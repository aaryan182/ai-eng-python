from typing import TypedDict

class PlanState(TypedDict):
    task: str
    plan: str
    route: str
    research_notes: str
    summary: str
    error: str
    retries: int
    final_output: str