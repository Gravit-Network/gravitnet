# 03-coordinator: Centralized Coordinator with Generation Barriers

**Status:** Accepted  
**Date:** 2026-04-08

## Context

Generation-based adversarial evolution requires consistent global progress across all nodes.

## Decision

Introduce a lightweight **Coordinator** node that:
- Assigns unique `generation_id`
- Broadcasts start of cycle
- Enforces **barrier** (waits for completion signals or timeout)
- Advances to next generation only when safe

## Why centralized coordinator?

- Ensures temporal ordering needed for anchors
- Simplifies failure detection and recovery
- Makes cycle boundaries explicit and verifiable

**Alternatives considered:** Fully decentralized consensus per cycle (rejected due to complexity and latency).

**Links:** 07-supersede-and-temporal-anchoring.md
