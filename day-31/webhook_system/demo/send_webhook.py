import requests
import json
import hmac
import hashlib

SECRET = "supersecret"
URL = "http://localhost:8000/webhook"

payload = {"job_id": 123, "status": "done"}
raw = json.dumps(payload).encode()

signature = hmac.new(
    SECRET.encode(),
    raw,
    hashlib.sha256,
).hexdigest()

headers = {
    "x-signature": signature,
    "x-event-id": "evt_001",
    "x-event-type": "job.completed",
}

r = requests.post(URL, json=payload, headers=headers)
print(r.json())
