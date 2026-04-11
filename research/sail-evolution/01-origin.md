# 01-origin: Why SAIL (Adversarial Co-Evolution Layer) Exists

**Status:** Accepted  
**Date:** 2026-04-08

## Context

Early verification approaches relied on static checks or random adversarial testing. Both proved insufficient for agentic AI systems that must maintain trust over long time horizons and under continuous pressure.

## Decision Drivers

- Need to move from "Trust = Signature" to "Trust = that which survives learned adversarial pressure"
- Requirement for self-improving verification (not just simulation)
- Alignment with GQRVP principle that true confidence must be earned through temporal stability under attack

## Decision

Introduce **SAIL** as a dedicated, mandatory layer (L4) between hypothesis generation and semantic conflict resolution.

## Consequences

SAIL transforms adversarial testing from an optional safety check into a core evolutionary mechanism of the entire system.

**Links:** 
- /research/distributed-execution/01-origin.md
- ADR-002: Make SAIL a Mandatory Layer
