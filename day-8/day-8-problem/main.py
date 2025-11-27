# Create an endpoint 
# POST /summarize
# Body: {"text": "..."}

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

class SummInput(BaseModel):
    text: str

@router.post("/summarize")
def summarize(data: SummInput):
    prompt = f"Summarize this in 3 bullet point: \n\n{data.text}"
    
    try: 
        response = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [{"role":"user", "content": prompt}]
        )
        return {"summary": response.choices[0].message["content"]}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))