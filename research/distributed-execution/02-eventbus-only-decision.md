# 02-decision: Adopt EventBus-only Communication (with selective gRPC)

**Status:** Accepted  
**Date:** 2026-04-08  
**Related ADR:** ADR-003

## Context

In a heterogeneous multi-node environment, direct synchronous calls create tight coupling and debugging nightmares.

## Decision Drivers

- Full traceability and auditability of reasoning cycles
- Ability to replay any generation for verification
- Decoupling between node types (Rust SAIL kernel vs Go SCE nodes)
- Compatibility with future History Keeper and temporal anchors

## Considered Options

| Option                  | Traceability | Scalability | Complexity | Latency |
|-------------------------|--------------|-------------|------------|---------|
| Full direct gRPC mesh   | Low          | Medium      | High       | Low     |
| Gossip protocol         | Medium       | High        | Very High  | Medium  |
| Pure EventBus           | Excellent    | High        | Medium     | Medium  |
| **Hybrid (EventBus + selective gRPC)** | Excellent | High     | Medium     | Acceptable |

## Decision

Primary communication channel is **EventBus-only** (NATS JetStream recommended, Kafka as alternative).  
Selective synchronous gRPC is allowed **only** to the Rust SAIL kernel for performance-critical operations (ComputeResilience, LearnFromFeedback).

## Consequences

All interactions become permanent events → direct support for GQRVP `Anchor(c)` and `𝒮(c)`.

**Links:** 01-origin.md, 07-supersede-and-temporal-anchoring.md
