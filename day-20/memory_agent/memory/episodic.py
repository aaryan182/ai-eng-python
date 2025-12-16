from .redis_client import get_json, set_json

def store_episode(user_id, summary):
    episodes = get_json(f"episodes: {user_id}") or []
    episodes.append(summary)
    set_json(f"episodes: {user_id}",episodes)

def get_episodes(user_id, limit=3):
    episodes = get_json(f"episodes: {user_id}") or []
    return episodes[-limit:]