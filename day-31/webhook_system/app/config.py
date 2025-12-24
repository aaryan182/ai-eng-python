import os

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "supersecret")
REDIS_QUEUE = "webhook:events"