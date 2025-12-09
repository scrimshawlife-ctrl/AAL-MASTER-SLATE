# AAL-Core Overview

AAL-Core is the "brainstem" of the Applied Alchemy Labs ecosystem. It is responsible for:

- coordinating communication between modules,
- routing symbolic and numeric data via the **ResonanceFrame** schema,
- managing lifecycle and health of each subsystem,
- enforcing systemic constraints like SEED and ABX-Core.

## Components

- **AAL Hub** – FastAPI-based service exposing HTTP/WebSocket endpoints and an internal message bus.
- **Module Adapters** – lightweight connectors that translate module-specific formats into ResonanceFrame.
- **Scheduler** – orchestrates long-running tasks, batch jobs, and streaming processes.
- **Registry** – keeps a catalog of available modules, their capabilities, and endpoints.

## Responsibilities

- ensure modules can be added or removed without breaking the ecosystem
- minimize coupling between symbolic engines and hardware infrastructure
- provide a single place for monitoring, logging, and observability
