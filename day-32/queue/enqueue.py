import json
import uuid
from queue.redis_client import redis_client

JOB_QUEUE = "jobs:main"

def enqueue_job(task: str, payload: dict):
    job = {
        "id": str(uuid.uuid4()),
        "task": task,
        "payload": payload,
    }
    redis_client.lpush(JOB_QUEUE, json.dumps(job))
