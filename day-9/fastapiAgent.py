from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import json

client = OpenAI()

router = APIRouter()


class Prompt(BaseModel):
    text: str


def get_weather(city):
    return f"The weather in {city}  is sunny"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    }
]


@router.post('/agent')
def run_agent(data: Prompt):
    first = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": data.text}],
        tools=tools
    )

    msg = first.choices[0].message

    if msg.tool_calls:
        call = msg.tool_calls[0]
        args = json.loads(call.function.arguments)

        result = get_weather(**args)

        second = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": data.text},
                msg,
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                }
            ]
        )
        return {"answer": second.choices[0].message["content"]}

    return {"answer": msg["content"]}
