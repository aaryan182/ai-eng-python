from typing import TypedDict, List

class AgentState(TypedDict):
    user_id: str
    input: str
    user_profile: dict
    episodes: List[str]
    response: str
    