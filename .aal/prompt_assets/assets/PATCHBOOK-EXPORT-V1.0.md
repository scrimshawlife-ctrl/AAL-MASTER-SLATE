# PATCHBOOK-EXPORT-V1.0

**PatchHive Global Patch Book Export Specification**

## Handle
`PH_EXPORT_v1`

## Status
Canonical

## Overview
The Global Patch Book is a consolidated, deterministic export of all patches in PatchHive, with configurable inclusion modes and visual styles.

## Architecture

### Inclusion Editions (Content)
Defined by `PH_INCLUSION_v1`. Controls what patches and metadata are included.
- Affects content
- Affects credit cost

### Visual Styles (Presentation)
Defined by `PH_STYLE_v1`. Controls typography, layout, color.
- Does NOT affect content
- Does NOT affect credit cost

### Separation of Concerns
Edition and style are orthogonal:
- User selects edition first (what to include)
- User selects style second (how to present)
- Export backend applies both independently

## Export Metadata
Every export must emit:
```json
{
  "export_id": "uuid",
  "timestamp": "ISO8601",
  "edition": "edition_name",
  "style": "style_name",
  "content_hash": "sha256",
  "sigil_version": "v0.3",
  "template_version": "v1.0",
  "patch_count": 123,
  "page_count": 45
}
```

## Determinism Requirements
- Same edition + same patches = identical content_hash
- Style changes DO NOT affect content_hash
- Exports are reproducible and cacheable

## Quote Generation
- Quotes are seeded from patch count or content hash
- Quotes appear on title page or section dividers
- Quote selection is deterministic per export

## Downstream Print Option
- Printing is a downstream action from export
- Reuses the same PDF artifact
- Does NOT fork the export process
- No independent print generation

## Omission Rules
- If a section has no data, omit it cleanly
- Do not show placeholders or "coming soon"
- Table of contents reflects actual present sections

## Non-Features
- No audio generation (scope boundary)
- No interactive elements (static PDF)
- No external data fetching (self-contained)
