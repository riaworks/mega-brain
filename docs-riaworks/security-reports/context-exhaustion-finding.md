# Finding: Context Window Exhaustion via Memory File Overload

**Repository:** `mega-brain` (thiagofinch/mega-brain)
**Date:** 2026-02-28
**Auditor:** Claude Opus 4.6 (Runtime Analysis)
**Severity:** MEDIUM (Operational Impact)
**Category:** Resource Exhaustion / Denial of Service (Self-Inflicted)
**Status:** OPEN

---

## Summary

The `.claude/rules/` directory contains 16 markdown files totaling **288KB raw / ~68,100 tokens**. These files are automatically loaded into the context window at session start as "memory files", consuming **34.1% of the total 200k token context** before any user interaction occurs.

Combined with system prompt (1.7%), system tools (7.9%), skills metadata (0.9%), and the autocompact buffer (16.5%), **over 61% of the context window is consumed before the first user message**.

This leaves only ~71k tokens (~35.6%) of effective working space for actual conversation, code reading, tool results, and agent work.

---

## Evidence

### Context breakdown (observed on session start)

| Category | Tokens | % of 200k |
|----------|--------|-----------|
| System prompt | 3,500 | 1.7% |
| System tools | 15,900 | 7.9% |
| **Memory files (rules)** | **68,100** | **34.1%** |
| Skills metadata | 1,800 | 0.9% |
| Autocompact buffer | 33,000 | 16.5% |
| **Free space** | **71,000** | **35.6%** |

### File sizes (raw bytes, sorted descending)

| File | Size (bytes) | Est. Tokens |
|------|-------------|-------------|
| agent-cognition.md | 64,707 | ~16,200 |
| agent-integrity.md | 34,403 | ~8,600 |
| RULE-GROUP-4.md | 32,952 | ~8,200 |
| ANTHROPIC-STANDARDS.md | 27,242 | ~6,800 |
| RULE-GROUP-6.md | 23,618 | ~5,900 |
| RULE-GROUP-5.md | 23,740 | ~5,900 |
| RULE-GROUP-3.md | 16,186 | ~4,000 |
| RULE-GROUP-2.md | 15,370 | ~3,800 |
| epistemic-standards.md | 15,308 | ~3,800 |
| RULE-GROUP-1.md | 12,108 | ~3,000 |
| CLAUDE-LITE.md | 9,606 | ~2,400 |
| RULE-GSD-MANDATORY.md | 4,205 | ~1,050 |
| mcp-governance.md | 4,079 | ~1,020 |
| state-management.md | 1,969 | ~490 |
| pipeline.md | 1,802 | ~450 |
| logging.md | 1,355 | ~340 |
| **TOTAL** | **288,650** | **~68,100** |

---

## Impact

### Operational
- **Reduced effective context:** Only 35.6% of context available for actual work
- **Earlier autocompaction:** Conversations hit the compaction threshold sooner, losing message history
- **Degraded multi-step tasks:** Complex tasks (code review, multi-file edits, agent operations) have significantly less room for tool results
- **Slower sessions:** More tokens processed per API call = higher latency and cost

### Architectural Contradiction
- `CLAUDE-LITE.md` documents a "lazy loading" strategy where rules are loaded on-demand via keyword matching by `skill_router.py`
- However, ALL 16 rule files are placed in `.claude/rules/` which Claude Code loads **eagerly** as memory files at session start
- The lazy loading intent is defeated by the file placement — the files are loaded regardless of keyword matching

### Cost
- At approximately $15/MTok (Opus input), the rules alone cost ~$1.02 per session start in input tokens
- This cost is incurred on every API round-trip as context is resent

---

## Root Cause

1. **All rules in `.claude/rules/`:** Claude Code treats every file in `.claude/rules/` as a memory file loaded at session start. There is no selective loading mechanism at this directory level.

2. **Redundant content:** Several rule files contain extensive ASCII art, box-drawing characters, and repeated structural patterns that inflate token count without adding semantic value.

3. **CLAUDE-LITE.md irony:** This file was created as a "lightweight" alternative (~9.6KB) but is loaded *in addition to* all the full rule files, not *instead of* them.

4. **No token budget:** There is no documented token budget or size limit for rule files.

---

## Recommendations

### R1: Move rules out of `.claude/rules/` (HIGH priority)

Move rule files that are meant for lazy loading to a different directory (e.g., `core/protocols/` or `.claude/lazy-rules/`) that is NOT auto-loaded by Claude Code. Keep only essential, always-needed rules in `.claude/rules/`.

**Target:** Reduce memory files from 68k to <15k tokens.

### R2: Consolidate and compress rule files (MEDIUM priority)

- Remove redundant ASCII art and box-drawing decorations
- Merge overlapping content (e.g., RULE-GROUP-1 through 6 into a single concise reference)
- Remove `agent-cognition.md` (64KB) and `agent-integrity.md` (34KB) from auto-load — these are agent protocols needed only during agent operations

### R3: Implement actual lazy loading (MEDIUM priority)

The `skill_router.py` hook already matches keywords to rule groups. Modify it to inject rule content via hook output only when matched, rather than relying on `.claude/rules/` auto-loading.

### R4: Set a token budget policy (LOW priority)

Add to CLAUDE.md:
```
## Rule File Policy
- Total .claude/rules/ budget: <15,000 tokens
- Individual rule file max: 3,000 tokens
- Use core/protocols/ for detailed references (loaded on demand)
```

---

## OWASP / Framework Mapping

| Framework | ID | Name | Relevance |
|-----------|----|----|-----------|
| OWASP LLM Top 10 | LLM10 | Unbounded Consumption | Self-inflicted resource exhaustion reducing effective context |
| MITRE ATLAS | AML.T0054 | LLM Resource Exhaustion | Internal configuration causing token waste |

---

## Upstream Action

This finding should be reported to the upstream repository (`thiagofinch/mega-brain`) as a **GitHub Issue**, not a PR, because:

1. It requires architectural discussion (where to put rules, how to implement lazy loading)
2. Multiple solution approaches exist (R1-R4 above)
3. The fix touches the project's core configuration philosophy
4. Repository maintainer input is needed before implementation

**Suggested issue title:** `[PERF] .claude/rules/ consumes 34% of context window on session start (68k/200k tokens)`

---

*Finding documented 2026-02-28 | Auditor: Claude Opus 4.6 | Method: Runtime observation via /context command*
