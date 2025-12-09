# Module Interoperability

This document explains how AAL modules communicate via AAL-Core and ResonanceFrame.

## Communication Principles

- **Loose Coupling** – Modules know about ResonanceFrame, not each other's internals.
- **Clear Contracts** – Each module documents its input and output frame structures.
- **Versioned Changes** – Changes to frame formats are versioned and tracked.

## Example Interactions

- Abraxas consumes symbolic + numeric data from HollerSports and emits overlays back.
- BeatOven takes emotional vectors from Abraxas and generates sonic structures.
- Noctis Engine outputs dream-derived symbols that Abraxas may incorporate into forecasts.
