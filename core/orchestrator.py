from engine.policy import policy_check
from engine.risk import compute_risk
from engine.decision import decide

def process_action(actor_id, action):
    context = {
        "market_volatility": 0.3,
        "agent_trust_score": 0.7
    }

    policy = policy_check(action)
    risk = compute_risk(action, context)
    decision = decide(policy, risk)

    return {
        "decision": decision,
        "risk": risk
    }
