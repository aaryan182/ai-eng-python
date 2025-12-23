import time

def process_job(job: dict):
    task = job["task_type"]
    
    if task == "send_email":
        time.sleep(1)
        print(f"[PROCESSOR] Email send to {job['payload']['to']}")
        return True
    
    if task == "fail_task":
        raise Exception("Simulated failure")
    
    raise Exception("unknown task")