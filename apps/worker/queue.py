import redis, json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def enqueue(action):
    r.lpush("gravit_queue", json.dumps(action))

def dequeue():
    _, data = r.brpop("gravit_queue")
    return json.loads(data)
