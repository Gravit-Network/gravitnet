# 04-node-types: Node Role Specialization

**Status:** Accepted  
**Date:** 2026-04-08

## Defined Node Types

- **Gateway Node** — ingress, validation, routing
- **SAIL Node** — attack generation + apply (calls Rust kernel via gRPC)
- **Attack Node** — specialized strategy learning
- **SCE Node** — conflict detection and reporting
- **Trust Node** — ResilienceScore + TrustProfile computation
- **Consensus Node** — weighted Byzantine consensus
- **Coordinator** — cycle orchestration (1–3 HA instances)
- **Observer Node** — metrics, audit, logging

## Rationale

Specialization improves observability, allows independent scaling, and keeps each node focused and testable.

**Links:** 01-origin.md
