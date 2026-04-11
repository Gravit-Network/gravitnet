# ADR-001: Establish Research Canon and Contribution Rules

**Status:** Accepted  
**Date:** 2026-04-08  
**Author:** Dr. Alex Konviser

## Context

Previous development produced strong technical artifacts, but important design decisions existed only in chat history, losing traceability and verifiability.

## Decision

We establish a formal `/research/` directory with strict Research Canon that enforces the flow:  
**Research (Why) → Specification (What) → Implementation (How)**.

All significant architectural decisions must be documented here before implementation.

## Consequences

Positive: Full traceability, better onboarding, verifiable history, alignment with GQRVP principles.  
Negative: Slight overhead in documentation.  
Risk: Over-documentation (mitigated by focused templates).

**Links:** /research/README.md
