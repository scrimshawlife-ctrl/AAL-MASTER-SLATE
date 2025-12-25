# PATCHBOOK-VISUAL-STYLES-v1.0

**PatchBook Visual Presentation Modes**

## Handle
`PH_STYLE_v1`

## Status
Canonical

## Purpose
Define visual presentation modes for Patch Books. Styles are content-invariant: they affect only typography, layout, and color.

## Core Principle
**Visual style MUST NOT affect content or credit cost.**

Same edition + different styles = identical content_hash

## Style Definitions

### 1. CLASSIC
**Serif, Traditional Layout**
- Font: Garamond or similar serif
- Margins: Generous (1.5" inner, 1" outer)
- Line spacing: 1.5
- Colors: Black text on white/cream
- Headers: Centered, small caps
- Page numbers: Centered footer
- Sigils: Minimal, elegant

### 2. MODERN
**Sans-Serif, Clean Layout**
- Font: Helvetica or similar sans-serif
- Margins: Balanced (1" all sides)
- Line spacing: 1.3
- Colors: Dark gray (#333) on white
- Headers: Left-aligned, bold
- Page numbers: Outer footer
- Sigils: Geometric, simple

### 3. COMPACT
**Dense, Reference Layout**
- Font: Small serif (9pt)
- Margins: Minimal (0.75" all sides)
- Line spacing: 1.2
- Colors: Black on white
- Headers: Inline, bold
- Page numbers: Outer header
- Sigils: Minimal or omitted
- Two-column option for patch listings

### 4. JOURNAL
**Handwritten Feel, Organic Layout**
- Font: Serif with handwriting-inspired headers
- Margins: Asymmetric (wider outer for notes)
- Line spacing: 1.4
- Colors: Warm black (#1a1a1a) on cream (#faf8f3)
- Headers: Hand-drawn style ornaments
- Page numbers: Varied placement
- Sigils: Organic, varied

## CSS/PDF Mapping
Each style maps to a CSS template or PDF generation profile:
```
CLASSIC   → templates/classic.css
MODERN    → templates/modern.css
COMPACT   → templates/compact.css
JOURNAL   → templates/journal.css
```

## Implementation Requirements
- Style selection happens AFTER edition selection
- Style application is a rendering-layer concern
- Content assembly is style-agnostic
- Export metadata includes style name but not in content_hash

## Preview System
Users should see style preview before export:
- Sample page with selected style
- Font/color/layout demonstration
- No content generation required for preview

## Future Extensibility
New styles can be added by:
1. Creating new CSS/template file
2. Adding style name to selection UI
3. No changes to content assembly logic
