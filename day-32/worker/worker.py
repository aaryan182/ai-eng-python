import json
import time
from queue.redis_client import redis_client
from worker.processor import process_job
from monitoring.metrics import record_success, record_failure

JOB_QUEUE = "jobs:main"

running = True

def worker_loop():
    print("[WORKER] Started")

    while running:
        _, raw = redis_client.brpop(JOB_QUEUE)
        job = json.loads(raw)

        try:
            process_job(job)
            record_success()
        except Exception as e:
            print("[WORKER] Error:", e)
            record_failure()

        time.sleep(0.1)

if __name__ == "__main__":
    worker_loop()
