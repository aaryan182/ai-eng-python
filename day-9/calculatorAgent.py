from openai import OpenAI
import json
client = OpenAI()


def add(a, b): return a + b
def subtract(a, b): return a - b


tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two integers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtract",
            "description": "Subtract b from a",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"]
            }
        }
    }
]


def agent(prompt):
    # Step 1: ask model
    first = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        tools=tools
    )

    msg = first.choices[0].message

    # Step 2: if tool call -> execute
    if msg.tool_calls:
        call = msg.tool_calls[0]
        args = json.loads(call.function.arguments)

        if call.function.name == "add":
            result = add(**args)
        elif call.function.name == "subtract":
            result = subtract(**args)

        # Step 3: return result to model
        second = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt},
                msg,
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                }
            ]
        )
        return second.choices[0].message["content"]

    return msg["content"]


print(agent("What is 10 - 3?"))
