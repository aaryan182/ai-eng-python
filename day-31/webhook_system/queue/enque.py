import json
from queue.redis_client import redis_client
from app.config import REDIS_QUEUE

def enqueue_event(event_id: str, job: dict):
    # Idempotency key
    key = f"webhook:event:{event_id}"

    if redis_client.exists(key):
        return  # already processed

    redis_client.set(key, "1", ex=86400)
    redis_client.lpush(REDIS_QUEUE, json.dumps(job))
