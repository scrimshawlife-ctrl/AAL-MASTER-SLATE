# BeatOven

## Overview
BeatOven is a psycho-sonic engine that turns emotional and symbolic vectors into music structures.

## Purpose
- Extract emotional vectors from reference tracks.
- Generate stems, MIDI, or CV/Gate signals.
- Tie sonic structures to symbolic intents and Abraxas overlays.

## Architecture
- Emotional feature extractor
- Symbolic-emotional mapping engine
- Generative layer for stems / MIDI / CV
- Output formatter for DAW-friendly or modular-friendly data

## IO Model
- Inputs: emotional descriptors, reference audio, symbolic tags, ResonanceFrames.
- Outputs: structured sonic blueprints, text descriptions, and metadata.

## Relationship to AAL-Core
BeatOven subscribes to symbolic/emotional frames from AAL Hub and publishes back sonic metadata and descriptors.

## Example Output (Text)
- "Generate a tempo-flexible techno stem set keyed to a 'resilience under pressure' vector, 126–130 BPM, minor modes, gradual build."
