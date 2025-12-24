import json
from queue.redis_client import redis_client
from app.config import REDIS_QUEUE

def worker_loop():
    print("[WORKER] Listening for webhook jobs")

    while True:
        _, raw = redis_client.brpop(REDIS_QUEUE)
        job = json.loads(raw)

        action = job["action"]
        data = job["data"]

        if action == "process_job":
            print("[WORKER] Processing completed job", data)

        elif action == "notify_admin":
            print("[WORKER] Notifying admin", data)
