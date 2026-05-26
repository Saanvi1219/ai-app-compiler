# Architecture

## Pipeline

```text
Natural Language Prompt
        ↓
Intent Extraction
        ↓
System Design Layer
        ↓
Schema Generation
        ↓
Validation Engine
        ↓
Repair Engine
        ↓
Runtime Simulation
        ↓
Executable App Config
```

## Components

### Intent Extraction

Converts raw user prompt into structured intermediate representation.

### System Design

Creates entities, roles, and flows.

### Schema Generation

Creates UI, API, DB, auth, and business logic config.

### Validation

Checks schema correctness and cross-layer consistency.

### Repair

Fixes specific broken layers instead of retrying the entire generation.

### Runtime Simulation

Simulates whether the config can produce pages, APIs, and tables.
