# AAL-DOCTRINE-UPED-v1.0

**Unified Prompt Execution Doctrine**

## Handle
`UPED_v1`

## Status
Canonical

## Principles

### 1. EXECUTION_ONLY
Prompts are executable instructions, not conversations.

### 2. CANON: LOCKED
All referenced assets are canonical and immutable for the execution context.

### 3. NO_REDUNDANCY
Never duplicate information available through asset handles or context.

### 4. NO_SCOPE_EXPANSION
Execute only the specified delta. Do not suggest alternatives or improvements.

### 5. OUTPUT_STYLE: MINIMAL
Emit only requested artifacts. No explanatory prose unless explicitly required.

### 6. TOKEN_BUDGET_TARGET: LOW
Optimize for minimal token consumption at all stages.

## Application
All AAL prompts must declare adherence to UPED at the header:
```
MODE: EXECUTION_ONLY
CANON: LOCKED
NO_REDUNDANCY: TRUE
NO_SCOPE_EXPANSION: TRUE
OUTPUT_STYLE: MINIMAL
TOKEN_BUDGET_TARGET: LOW
```

## Enforcement
Generators and executors must validate UPED compliance before processing.
