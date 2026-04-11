# 01-origin: Why We Need a Distributed Execution Layer

**Status:** Accepted  
**Date:** 2026-04-08  
**Related ADR:** ADR-003, ADR-004

## Context

The single-process Rust implementation (GCES Kernel v4.2) successfully demonstrated SAIL Engine, ResilienceScore computation, and the adversarial-conflict loop. However, it revealed fundamental scaling and operational limitations:

- No horizontal scalability for real agentic workloads
- Lack of fault isolation between SAIL, SCE, and Trust components
- Difficulty maintaining long-running generation cycles with temporal consistency
- Challenges integrating heterogeneous components (Rust performance kernel + future Go/Python nodes)

## Decision Drivers

- Requirement for true horizontal scalability
- Need for strong isolation and observability
- Alignment with GQRVP requirements for temporal persistence and verifiable history
- Support for multi-language implementation without tight coupling

## Decision

Introduce **GCES Distributed Execution Layer v5.0** as L8 of the architecture — a multi-node system with specialized roles communicating primarily via EventBus.

## Consequences

Positive: Scalability, fault isolation, replayability, easier evolution of individual components.  
Negative: Increased operational complexity and need for coordination.  
Risk: Coordinator becoming a bottleneck (mitigated by HA design and stateless nodes).

**Links:**
- /specs/distributed-execution.md (forthcoming)
- /research/distributed-execution/08-gravit-triad-mapping.md
