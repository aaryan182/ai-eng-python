from pydantic import BasesModel

class SummarizeInput(BasesModel):
    text: str