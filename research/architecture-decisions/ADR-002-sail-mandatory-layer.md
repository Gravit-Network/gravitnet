# ADR-002: Make SAIL a Mandatory Layer (L4)

**Status:** Accepted  
**Date:** 2026-04-08

## Context

Early versions treated adversarial testing as optional. This weakened the verification guarantees.

## Decision

SAIL (Adversarial Co-Evolution Layer) becomes **mandatory**. No hypothesis may proceed to SCE or Consensus without passing SAIL stress and producing `ResilienceMetrics`.

## Consequences

This directly implements the core idea of GQRVP: Trust = that which survives learned adversarial pressure.

**Links:** /research/sail-evolution/ (future), /specs/GQRVP.md
