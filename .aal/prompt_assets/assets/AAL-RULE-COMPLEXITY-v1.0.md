# AAL-RULE-COMPLEXITY-v1.0

**Complexity Rule**

## Handle
`COMPLEXITY_v1`

## Status
Canonical

## Rule Statement
**Never duplicate canon. Reference the single source of truth.**

## Application

### For Repositories
When multiple repos need the same specification:
- ❌ Copy specification to each repo
- ✅ Reference canonical specification from master source

### For Prompts
When multiple prompts need the same rules:
- ❌ Inline rules in each prompt
- ✅ Reference asset handle from Prompt Asset Registry

### For Code
When multiple modules need the same logic:
- ❌ Duplicate implementation
- ✅ Import from canonical module

### For Documentation
When multiple documents need the same content:
- ❌ Copy content to each document
- ✅ Reference canonical document

## Examples

### Bad (Duplicates Canon)
```
PROMPT A contains full sigil spec
PROMPT B contains full sigil spec
```

### Good (References Canon)
```
PROMPT A: CANON_ASSETS: [PH_SIGIL_v0_3]
PROMPT B: CANON_ASSETS: [PH_SIGIL_v0_3]
```

## Rationale
Duplication creates:
- Maintenance burden (update N places)
- Inconsistency risk (versions drift)
- Token waste (same text repeated)
- Cognitive load (which version is authoritative?)

Single source of truth eliminates all of these.
