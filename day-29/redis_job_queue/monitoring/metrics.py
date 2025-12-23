success = 0
failure = 0

def record_success():
    global success
    success += 1
    print(f"[METRICS] success={success}")

def record_failure():
    global failure
    failure += 1
    print(f"[METRICS] failure={failure}")