import json
from queue.redis_client import redis_client
from queue.queues import RETRY_QUEUE, DEAD_QUEUE, MAX_RETRIES

def handle_retry(job):
    job["retries"] += 1

    if job["retries"] > MAX_RETRIES:
        redis_client.lpush(DEAD_QUEUE, json.dumps(job))
        print(f"[RETRY] Job {job['id']} moved to DEAD queue")
    else:
        redis_client.lpush(RETRY_QUEUE, json.dumps(job))
        print(f"[RETRY] Job {job['id']} retry #{job['retries']}")