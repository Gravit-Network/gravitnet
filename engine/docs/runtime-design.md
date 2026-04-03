# Gravit Engine Runtime Design

Version: 0.4

This document describes the current internal design of the runtime.

---

## Core Loop (step)

1. Generate signals (with phase-aware behavior)
2. Apply trust-weighted + asymmetric signals
3. Apply decay
4. Propagate reputation
5. Apply penalties (Sybil, collusion, scar, behavior)
6. Update breach state & tiers
7. Record metrics & update RL policy

---

## Key Mechanisms Implemented

• Trust Memory (historical stability)
• Irreversible scars (breach_flag + slow fade)
• Phase-aware anomaly detection
• Reputation tiers (operational levels)
• Adaptive adversary policy + RL scaffold

---

## Extensibility Points

• Add new action in RL_ACTIONS
• Extend behavior classification
• Plug in different RL algorithms (PPO, DQN)
• Add new tier transition rules

---

## Current Limitations (v0.4)

• No real network (only simulation mode)
• No persistent storage
• Simple Q-table (easy to replace)

---

## Next Milestones

• Full RL training loop
• Defense adaptation module
• Multi-node coordination
• Export to production engine
