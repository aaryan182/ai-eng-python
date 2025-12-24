import datetime

def audit_log(event: str, meta: dict):
    ts = datetime.datetime.utcnow().isoformat()
    print(f"[AUDIT] {ts} | {event} | {meta}")
