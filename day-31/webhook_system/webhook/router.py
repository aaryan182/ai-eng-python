def route_event(event_type:  str, data: dict):
    if event_type == "job.completed":
        return {"action": "process_job", "data": data}
    
    if event_type == "human.review":
        return {"action": "notify_admin", "data": data}
    
    return {"action": "ignore", "data": data}
