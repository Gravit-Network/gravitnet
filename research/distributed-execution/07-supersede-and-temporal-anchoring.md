# 07-supersede-and-temporal-anchoring: State Supersession Logic

**Status:** Accepted  
**Date:** 2026-04-08

## Problem

How do we safely replace old hypothesis states with new, evolved ones without breaking temporal consistency?

## Decision

- Each generation produces a new `Anchor(c)` with `generation_id`
- Supersession happens only when `ResilienceScore(new) > ResilienceScore(old) + δ` and Consensus approves
- Old anchors are never deleted — they remain part of the verifiable history

This directly implements GQRVP `𝒮(c)` integral stability metric.

**Links:** 03-coordinator-model.md
