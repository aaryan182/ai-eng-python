from .redis_client import get_json, set_json

def get_user_profile(user_id):
    return get_json(f"user: {user_id}") or {}

def update_user_profile(user_id, updates):
    profile = get_user_profile(user_id)
    profile.update(updates)
    set_json(f"user:{user_id}", profile)