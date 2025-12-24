from limiter.token_bucket import consume_token

IP_CAPACITY = 20
IP_REFILL_RATE = 0.5

def allow_ip(ip: str) -> bool:
    key = f"rate:ip:{ip}"
    return consume_token(
        key=key,
        capacity=IP_CAPACITY,
        refill_rate=IP_REFILL_RATE,
    )