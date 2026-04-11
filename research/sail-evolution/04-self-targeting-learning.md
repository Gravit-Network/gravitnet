# 04-self-targeting-learning: From Random Attacks to Adaptive Self-Targeting

**Status:** Accepted  
**Date:** 2026-04-08

## Context

Random attack generation does not scale to sophisticated adversaries.

## Decision

SAIL uses adaptive strategy weights updated based on `weakest_dimension` from ResilienceMetrics and ConflictReportEvent.

If a dimension (e.g. semantic) shows low stability, the weight of corresponding attack strategies is increased.

## Consequences

This creates a true co-evolution loop: the system learns to attack its own current weaknesses.

**Links:** 05-sce-integration.md
