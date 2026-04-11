# ADR-003: Adopt EventBus-only Communication in Distributed Layer

**Status:** Accepted  
**Date:** 2026-04-08

## Context

Heterogeneous multi-node system requires loose coupling and full auditability.

## Decision

Primary communication is **EventBus-only**. Selective gRPC is allowed only to the Rust SAIL kernel for performance-critical calls.

## Consequences

Excellent traceability and replayability, direct support for temporal anchors.

**Links:** /research/distributed-execution/02-eventbus-only-decision.md
