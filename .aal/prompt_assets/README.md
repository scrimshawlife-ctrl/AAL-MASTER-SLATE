# AAL Prompt Asset Registry

## Purpose
Canonical source of truth for all AAL prompt assets, doctrines, and specifications.

## Structure
```
.aal/prompt_assets/
├── registry.json          # Asset index and metadata
├── assets/                # Canonical asset files
│   ├── AAL-DOCTRINE-*.md  # Core doctrines
│   ├── AAL-RULE-*.md      # System rules
│   └── PATCHBOOK-*.md     # PatchHive specifications
└── templates/             # Executable prompt templates
    └── PH_*.txt           # PatchHive prompt templates
```

## Registry Format
`registry.json` contains:
- Asset handles (unique identifiers)
- Version tracking
- File locations
- Asset metadata (title, description, status)

## Usage

### In Prompts
Reference assets by handle:
```
CANON_ASSETS:
- UPED_v1
- COPD_v1
- PH_EXPORT_v1
```

### Adding New Assets
1. Create asset file in `assets/`
2. Add entry to `registry.json`
3. Assign unique handle with version
4. Mark status as `canonical` when approved

### Updating Assets
1. Create new version file (e.g., `v1.1`)
2. Add new entry to `registry.json`
3. Update dependent prompts to reference new version
4. Archive old version (do not delete)

## Sync Protocol
This is a **mirror** of the canonical Prompt Asset Registry.

When assets are updated in the canonical source:
1. Pull latest changes
2. Validate `registry.json` schema
3. Verify all referenced files exist
4. Update dependent repositories

## Enforcement
All AAL prompts MUST:
- Reference assets by handle (never inline)
- Declare CANON_ASSETS at prompt header
- Follow UPED and COPD doctrines
