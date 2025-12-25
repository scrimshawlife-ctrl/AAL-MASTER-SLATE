# PATCHBOOK-SIGIL-SYSTEM-v0.3

**PatchBook Sigil Grammar**

## Handle
`PH_SIGIL_v0_3`

## Status
Canonical

## Purpose
Deterministic, content-aware decorative patterns for patch book headers, dividers, and ornaments.

## Grammar Rules

### Pattern Elements
- `#` : Heavy block
- `·` : Light dot
- `─` : Horizontal line
- `│` : Vertical line
- `╱` : Diagonal ascent
- `╲` : Diagonal descent

### Composition Rules
1. Maximum pattern width: 60 characters
2. Patterns must be horizontally symmetric
3. Vertical patterns limited to 5 lines
4. No orphaned elements (all elements must connect visually)

### Determinism
Sigil selection is seeded by:
- Patch count (for collection-level sigils)
- Content hash modulo (for section-level sigils)
- Edition name hash (for title page sigil)

### Example Patterns
```
Title Page (Edition-seeded):
#═══════════════════════════════════════════════════#

Section Divider (Content-seeded):
─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─

Chapter Header (Patch-count-seeded):
    ╱╲
   ╱  ╲
  ╱    ╲
```

### Constraints
- Sigils use ASCII/extended ASCII only (PDF-safe)
- No emoji or Unicode symbols outside printable range
- Background compatibility: must work on white and cream backgrounds

## Version Tracking
All exports must record sigil version in metadata:
```
"sigil_version": "v0.3"
```

## Future Compatibility
When upgrading sigil grammar:
- New version handle (e.g., `PH_SIGIL_v0_4`)
- Exports reference specific version
- Historical exports remain reproducible with their grammar version
