import json
import time

from queue.redis_client import redis_client
from queue.queues import JOB_QUEUE, RETRY_QUEUE
from worker.processor import process_job
from worker.retry import handle_retry
from monitoring.metrics import record_success, record_failure

def consume(queue_name):
    _, raw = redis_client.brpop(queue_name)
    return json.loads(raw)

def worker_loop():
    print("[WORKER] Started")

    while True:
        job = consume(JOB_QUEUE)

        try:
            process_job(job)
            record_success()
            print(f"[WORKER] Job {job['id']} done")

        except Exception as e:
            print(f"[WORKER] Job {job['id']} failed: {e}")
            record_failure()
            handle_retry(job)

        time.sleep(0.1)

if __name__ == "__main__":
    worker_loop()