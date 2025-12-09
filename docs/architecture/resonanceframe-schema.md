# ResonanceFrame Schema

ResonanceFrame is the shared data envelope that moves through the AAL ecosystem.

## Key Fields (Conceptual)

- **id** – unique identifier for the frame
- **source** – which module or external system produced it
- **timestamp** – when the frame was generated
- **numeric_vectors** – structured numeric data (metrics, probabilities, etc.)
- **symbolic_vectors** – tags, archetypes, sigils, narrative markers
- **context** – optional human-readable context or notes
- **links** – references to other frames or external entities

## Design Goals

- Be flexible enough to represent different domains.
- Stay structured enough for automation, indexing, and forecasting.
- Provide a common backbone for symbolic and numeric data.
