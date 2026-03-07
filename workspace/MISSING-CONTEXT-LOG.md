# Missing Context Log

> **Purpose:** Track business context gaps detected by agents during sessions.
> **Location:** `knowledge/workspace/MISSING-CONTEXT-LOG.md`
> **Updated by:** JARVIS and cargo agents when they detect missing business data.

## How This Works

When an agent needs business context to answer a question but cannot find it in
`knowledge/workspace/`, it logs the gap here. This creates a backlog of information
that should be imported into the workspace bucket.

## Format

Each entry follows this structure:

```
### YYYY-MM-DD -- [Category]
- **Detected by:** [Agent name]
- **Context needed:** [What was missing]
- **Why needed:** [What question triggered the detection]
- **Suggested source:** [Where this data might come from]
- **Priority:** [HIGH / MEDIUM / LOW]
- **Status:** [OPEN / RESOLVED / WONT-FIX]
```

## Log Entries

_No entries yet. Gaps will be logged here as agents detect missing business context._
