from fastapi import APIRouter, HTTPException
from models.chat_model import ChatInput
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

router = APIRouter()

@router.post("/chat")
def chat(data: ChatInput):
    try:
        response = client.chat.completions.create(
        model= "gpt-4.1-mini",
        messages=[{"role": "user", "content": data.prompt}]
        )
        answer = response.choices[0].message["content"]
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code = 500, detail= str(e))