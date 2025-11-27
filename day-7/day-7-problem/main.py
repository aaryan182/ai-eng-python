# Build POST /wordcount 
# BODY: {"text": "..."}
# Responses: {"count": <number> }


from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class WordInput(BaseModel):
    text: str

@router.post("/wordcount")
def wordcount(data: WordInput):
    count = len(data.text.split())
    return {"count": count}

