# AAL-DOCTRINE-COPD-v1.0

**Canon-Only Prompt Design**

## Handle
`COPD_v1`

## Status
Canonical

## Core Principle
Prompts reference canon; they do not contain canon.

## Rules

### 1. Asset References Only
All prompts must reference assets by handle from the Prompt Asset Registry.

Never inline specifications, doctrines, or rules directly into prompts.

### 2. Single Delta Per Prompt
Each prompt specifies exactly one delta (change/action).

Do not combine multiple independent deltas in a single prompt.

### 3. CANON_ASSETS Declaration
All prompts must declare their canonical dependencies:
```
CANON_ASSETS:
- UPED_v1
- COPD_v1
- [additional asset handles]
```

### 4. DELTA Section
Prompts must include a DELTA section that specifies:
- What changes/additions are required
- Which files/artifacts are affected
- Scope boundaries

## Example Structure
```
MODE: EXECUTION_ONLY
CANON: LOCKED

CANON_ASSETS:
- UPED_v1
- COPD_v1
- SPEC_FOO_v2

DELTA:
Add feature X to module Y following SPEC_FOO_v2 patterns.

FILES TO MODIFY:
- src/module_y.py
```

## Benefits
- Eliminates prompt bloat
- Ensures canonical consistency
- Enables version tracking
- Simplifies updates to shared specifications
