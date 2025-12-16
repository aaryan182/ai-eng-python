from llm.client import call_llm
from memory.long_term import get_user_profile, update_user_profile
from memory.episodic import get_episodes, store_episode


def load_memory_node(state):
    state["user_profile"] = get_user_profile(state["user_id"])
    state["episodes"] = get_episodes(state["user_id"])
    return state

def respond_node(state):
    rompt = f"""
User profile:
{state['user_profile']}

Recent interactions:
{state['episodes']}

User says:
{state['input']}

Respond helpfully.
"""
    response = call_llm(prompt)
    state["response"] = response
    return state

def update_memory_node(state):
    # Example: store episodic summary
    episode_summary = f"User said: {state['input']} | Agent replied."
    store_episode(state["user_id"], episode_summary)

    # Example preference update
    if "formal" in state["input"].lower():
        update_user_profile(state["user_id"], {"prefers_formal": True})

    return state