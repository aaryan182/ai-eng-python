import time
from limiter.redis_client import redis_client

def consume_token(key:str, capacity: int, refill_rate: float) -> bool:
    """
    Atomic Token bucket using redis.
    capacity: max tokens
    refill_rate: tokens per second
    """
    now = time.time()
    
    pipe = redis_client.pipeline()
    pipe.hgetall(key)
    data = pipe.execute()[0]
    
    tokens = float(data.get("tokens", capacity))
    last_refill = float(data.get("last_refill", now))
    
    # Refill tokens
    delta = now - last_refill
    tokens = min(capacity, tokens + delta * refill_rate)
    
    if tokens < 1: 
        return False  # rate limited
    
    tokens -= 1
    
    # save state
    redis_client.hset(
        key,
        mapping = {
            "tokens": tokens,
            "last_refill": now,
        },
    )
    redis_client.expire(key, 3600)
    
    return True