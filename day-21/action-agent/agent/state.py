from typing import TypedDict, Any

class ActionState(TypedDict):
    user_input: str
    action: str
    tool_input: dict
    observation: Any
    final_output: str

