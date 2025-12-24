import time

def process_job(job: dict):
    print("[PROCESSOR] Processing job", job["id"])
    time.sleep(2) # simulate heavy work
    print("[PROCESSOR] Done", job["id"])