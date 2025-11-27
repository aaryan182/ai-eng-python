from fastapi import APIRouter
from models.summarize_model import SummarizeInput

router = APIRouter

@router.post("/summarize")
def summarize(data: SummarizeInput):
    words = data.text.split()
    summary = " ".join(words[:10]) + "..."
    return {"summary": summary}

