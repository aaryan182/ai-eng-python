from limiter.token_bucket import consume_token

USER_CAPACITY = 10       # burst
USER_REFILL_RATE = 1.0  # tokens/sec

def allow_user(user_id: str) -> bool:
    key = f"rate:user:{user_id}"
    return consume_token(
        key=key,
        capacity=USER_CAPACITY,
        refill_rate=USER_REFILL_RATE,
    )