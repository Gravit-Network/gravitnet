# Gravit Open Network — Research Canon

This directory contains the **research and architectural decision history** of the Gravit Open Network project.

It serves as the **source of truth** for *why* we made specific architectural and technical decisions.

## Purpose

The `/research/` directory captures:
- The origin and motivation behind major design choices
- Trade-off analysis and considered alternatives
- Evolution of ideas (how decisions changed over time)
- Connection points to the formal specifications and implementation

This ensures **traceability**, **verifiability**, and **temporal stability** — core principles of the Gravit Quantum Resilient Verification Protocol (GQRVP).

## Core Principles

1. **Research → Specification → Implementation**
   Every significant component must follow this flow:
   - **Research**: Why we chose this path (forces, alternatives, risks)
   - **Specification**: What exactly we decided (formal definition)
   - **Implementation**: How it is realized (code, prototypes)

2. **No Decision Without Trace**
   Important decisions must not exist only in chat history or "packages". They must be documented here first.

3. **Living Canon**
   Research documents are versioned through status and supersession. Old decisions can be deprecated or superseded, but never deleted.

4. **Cross-referencing**
   Every research document must link to:
   - Related ADR entries
   - Corresponding specifications (`/specs/`)
   - Implementation code (`/core/`, `/engine/`)

## Directory Structure

```text
/research/
├── README.md                          # This file — Research Canon
├── architecture-decisions/            # Architecture Decision Records (ADR)
├── distributed-execution/             # Distributed layer (GCES v5.0)
├── sail-evolution/                    # SAIL Engine and adversarial co-evolution
├── trust-computation/                 # Trust Engine evolution
├── gqrvp-core/                        # Core GQRVP development history
├── experiments/                       # Benchmarks, stress tests, empirical results
└── alternatives/                      # Comparisons with other approaches
