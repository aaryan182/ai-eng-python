from limiter.user_limiter import allow_user
from limiter.ip_limiter import allow_ip

class RateLimitError(Exception):
    pass

def rate_limit(user_id: str, ip: str):
    if not allow_ip(ip):
        raise RateLimitError("IP rate limit exceeded")

    if not allow_user(user_id):
        raise RateLimitError("User rate limit exceeded")