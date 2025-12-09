# Defining the langgraph state 

from typing import TypedDict

class EmailState(TypedDict):
    user_input: str
    intent: str
    rewritten: str
    final_email: str
    