# Gravit Core Canon

## Math Core — Parameters

**Version:** 0.1
**Status:** Canonical Baseline
**Last updated:** 2026-03-16

This document defines the default operational calibration of the Gravit Trust Protocol.
Parameters do **not** define the architecture — only its tuning.
All parameters MAY evolve through governance procedures defined in `/governance`.

---

### 1. Trust Aggregation Weights

The trust score of node \( i \) at time \( t \) is:

$$
\tau_i(t) = \alpha p_i + \beta s_i + \gamma r_i + \delta m_i
$$

where \( p_i, s_i, r_i, m_i \in [0,1] \) and

$$
\alpha + \beta + \gamma + \delta = 1
$$

**Default values:**

- \( \alpha = 0.35 \) (performance)
- \( \beta = 0.25 \) (signal credibility)
- \( \gamma = 0.25 \) (propagated reputation)
- \( \delta = 0.15 \) (meta-confidence)

**Rationale:** Performance receives the highest weight to disincentivize pure reputation farming.

---

### 2. Temporal Decay Coefficient

Every trust component decays exponentially in the absence of new reinforcement:

$$
x_i(t) = x_i(t_0) \, e^{-\lambda (t - t_0)}
$$

**Default:** \( \lambda = 0.015 \) (per time unit)

**Interpretation:** Approximate half-life \( \frac{\ln 2}{\lambda} \approx 46.2 \) time units.
Decay prevents historical reputation monopolies (see `/ontology`).

---

### 3. Trust Propagation Coefficient

Reputation update rule:

$$
r_i^{\text{new}} = (1 - \eta) r_i + \eta \sum_{j \in N} W_{ji} \tau_j
$$

**Default:** \( \eta = 0.30 \)

**Interpretation:** 30% of reputation is influenced by the network. Lower \( \eta \) increases stability; higher \( \eta \) increases responsiveness.

---

### 4. Influence Matrix Normalization

$$
W_{ij} = \frac{w_{ij}}{\sum_k w_{ik}}
$$

**Constraints:**

$$
0 \leq W_{ij} \leq 1, \quad \sum_j W_{ij} = 1
$$

---

### 5. Threshold Configuration

- Warning threshold: \( \theta_w = 0.55 \)
- Quarantine threshold: \( \theta_q = 0.35 \)
- Recovery threshold: \( \theta_r = 0.65 \)

**State transitions** (see state machine in `/protocol`):

- \( \tau_i \geq \theta_r \) → NORMAL
- \( \theta_q \leq \tau_i < \theta_w \) → WARNING
- \( \tau_i < \theta_q \) → QUARANTINED

---

### 6. Quarantine Recovery Coefficient

In RECOVERING state the effective influence is scaled:

$$
\tau_i^{\text{effective}} = \kappa \tau_i
$$

**Default:** \( \kappa = 0.20 \)

---

### 7. Sybil Density Limit

Node connection density:

$$
D_i = \frac{|E_i|}{|N|}
$$

If \( D_i > \rho_{\max} \), apply penalty:

$$
\tau_i := \tau_i (1 - \sigma)
$$

**Defaults:** \( \rho_{\max} = 0.08 \), \( \sigma = 0.40 \)

---

### 8. Collusion Sensitivity

A subgraph \( G' \) is flagged as collusion candidate when the ratio of internal to external edge density exceeds:

$$
C = \frac{|E_{\text{in}}| / |G'|^2}{|E_{\text{out}}| / (|G'| \cdot |N \setminus G'|)} \geq 3
$$

**Default threshold:** \( C \geq 3 \)

---

### 9. Meta-Confidence Weights

$$
m_i^{\text{new}} = \phi_1 \cdot \text{consistency} + \phi_2 \cdot \text{verification} + \phi_3 \cdot \text{historical stability}
$$

**Constraint:** \( \phi_1 + \phi_2 + \phi_3 = 1 \)

**Defaults:**
- \( \phi_1 = 0.40 \)
- \( \phi_2 = 0.35 \)
- \( \phi_3 = 0.25 \)

---

### 10. Parameter Governance

All parameters in this document are:
- version-controlled
- governance-adjustable
- simulation-validated

Changes require:
1. Protocol proposal
2. Simulation evidence (see `/simulations`)
3. Governance quorum approval

---

**Canon Notice**
This document defines **operational defaults only**.
Architectural definitions reside in:
- `/ontology`
- `/epistemology`
- `/protocol`
- `/threat-model`

Parameters may evolve without altering the structural invariants of the Gravit Core Canon.
