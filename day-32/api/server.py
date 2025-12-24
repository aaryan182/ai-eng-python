from fastapi import FastAPI
from queue.enqueue import enqueue_job

app = FastAPI()

@app.post("/process")
def process(payload: dict):
    enqueue_job("heavy_task", payload)
    return {"status": "queued"}


# This server:

# Returns immediately
# Never blocks
# Scales independently of workers