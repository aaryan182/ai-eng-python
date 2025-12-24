import hmac
import hashlib
from app.config import WEBHOOK_SECRET

def verify_signature(payload: bytes, signature: str) -> bool:
    computed = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256,
    ).hexdigest()
    
    return hmac.compare_digest(computed, signature)