# 02-decision: Make SAIL a Mandatory Layer (L4)

**Status:** Accepted  
**Date:** 2026-04-08  
**Related ADR:** ADR-002

## Context

In previous iterations adversarial evaluation was treated as optional post-processing.

## Decision

No hypothesis may proceed to SCE (Semantic Conflict Engine) or Trust/Consensus without successfully passing SAIL and producing a valid `ResilienceMetrics` record.

## Rationale

This enforces the central GQRVP idea:  
**Truth(c) = integral stability under continuous, learned adversarial pressure.**

## Consequences

- Stronger soundness guarantees
- Self-targeting attack strategies become possible
- Increased computational cost per hypothesis (accepted trade-off)

**Links:** /specs/GQRVP.md, 01-origin.md
