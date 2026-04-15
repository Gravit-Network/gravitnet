# Security Model

## Threat Model

- adversarial hypothesis injection
- event replay attacks
- consensus manipulation
- trace corruption attempts

## Guarantees

- trace immutability (Ω layer)
- bounded adversarial model (κ-limited)
- deterministic execution per generation

## Redteam Policy

All major changes must pass adversarial simulation before production merge.
