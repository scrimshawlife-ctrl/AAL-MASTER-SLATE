# PATCHBOOK-INCLUSION-MODES-v1.0

**PatchBook Inclusion Editions**

## Handle
`PH_INCLUSION_v1`

## Status
Canonical

## Purpose
Define what patches and metadata are included in different editions of the Patch Book.

## Edition Definitions

### 1. CORE
**Patches Only**
- All approved patches (full text)
- Minimal metadata (title, date, author)
- No commentary, no lineage, no analytics
- Smallest file size, lowest credit cost

### 2. ANNOTATED
**Patches + Context**
- All approved patches (full text)
- Full metadata (title, date, author, tags, status)
- Patch lineage (parent/child relationships)
- Cross-references between related patches
- Medium file size, medium credit cost

### 3. COMPLETE
**Everything**
- All approved patches (full text)
- Full metadata (as in ANNOTATED)
- Patch lineage and relationships
- Analytics summaries (tag frequency, author stats, timeline)
- Appendices (tag index, author index, chronological index)
- Largest file size, highest credit cost

### 4. CURATED
**Selected Patches Only**
- User-selected subset of patches
- Full metadata for included patches
- Lineage limited to included patches
- Variable file size, variable credit cost

## Metadata Inclusion Matrix

| Element | CORE | ANNOTATED | COMPLETE | CURATED |
|---------|------|-----------|----------|---------|
| Patch text | ✓ | ✓ | ✓ | ✓ |
| Title/Date/Author | ✓ | ✓ | ✓ | ✓ |
| Tags | - | ✓ | ✓ | ✓ |
| Status | - | ✓ | ✓ | ✓ |
| Lineage | - | ✓ | ✓ | ✓* |
| Cross-refs | - | ✓ | ✓ | ✓* |
| Analytics | - | - | ✓ | - |
| Indices | - | - | ✓ | - |

*Curated: limited to included patches only

## UI Selection Flow
1. User selects edition (CORE, ANNOTATED, COMPLETE, or CURATED)
2. If CURATED: user selects specific patches
3. System calculates estimated page count and credit cost
4. User confirms and initiates export

## Credit Cost Formula
```
base_cost = patch_count × 10 credits
metadata_multiplier = 1.0 (CORE), 1.5 (ANNOTATED), 2.0 (COMPLETE), variable (CURATED)
final_cost = base_cost × metadata_multiplier
```

## Implementation Notes
- Edition selection affects backend query and assembly
- Visual style does NOT affect inclusion (orthogonal)
- Missing data: omit section cleanly (no placeholders)
