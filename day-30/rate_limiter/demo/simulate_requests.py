import time
from middleware.rate_limit import rate_limit, RateLimitError

USER = "user_123"
IP = "192.168.1.10"

for i in range(25):
    try:
        rate_limit(USER, IP)
        print(f"[{i}] Request allowed")
    except RateLimitError as e:
        print(f"[{i}] BLOCKED → {e}")

    time.sleep(0.2)