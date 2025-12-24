import json
from webhook.router import route_event
from queue.enque import enqueue_event
from audit.logger import audit_log

def handle_webhook(event_id: str, event_type: str, payload: dict):
    """
    Idempotency:
    - event_id should be unique from sender
    - redis set ensures no double processing
    """
    
    audit_log("WEBHOOK_RECIEVED", {"event_id": event_id})
    
    job = route_event(event_type, payload)
    enqueue_event(event_id, job)
    
    audit_log("WEBHOOK_ENQUEUED": {"event_id": event_id})