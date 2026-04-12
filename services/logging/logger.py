from .db import get_conn
import json

def log_action(actor_id, action, decision, risk):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO actions (actor_id, action_type, payload, decision, risk_score)
    VALUES (%s, %s, %s, %s, %s)
    """, (
        actor_id,
        action["type"],
        json.dumps(action["payload"]),
        decision,
        risk
    ))

    conn.commit()
