# HollerSports

## Overview
HollerSports is a forecasting and parlay-planning system for sports events.

## Purpose
- Generate high-quality parlays and prop selections.
- Model risk through Conservative, Balanced, and Aggressive templates.
- Integrate symbolic overlays from Abraxas for narrative context.

## Architecture
- Data ingestion from sports APIs (conceptual)
- Statistical baseline model
- Parlay and prop builder
- Risk profiling layer
- Abraxas overlay integration

## IO Model
- Inputs: sports statistics, schedules, historical data, ResonanceFrames.
- Outputs: parlay suggestions, hit-rate estimates, ROI simulations, symbolic overlays.

## Relationship to AAL-Core
HollerSports is orchestrated as a module process that publishes and consumes ResonanceFrames via AAL Hub.

## Example Output (Text)
- Bettor Console readouts with % hit, ROI, and symbolic tags like "momentum," "fatigue," or "variance skew."
