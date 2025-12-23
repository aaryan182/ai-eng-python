import json
import uuid
from queue.redis_client import redis_client
from queue.queues import JOB_QUEUE

def enqueue_job(task_type: str, payload: dict):
    job= {
        "id": str(uuid.uuid4()),
        "task_type": task_type,
        "payload": payload,
        "retries": 0,
    }
    redis_client.lpush(JOB_QUEUE, json.dumps(job))
    print(f"[PRODUCER] Enqueued job {job['id']}")
    
if __name__ == "__main__":
    enqueue_job(
        "send_email",
        {"to": "aaryan@gmail.com", "subject": "Hello"}
    )