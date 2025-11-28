# User sends a text like

# My name is Aaryan Bajaj. I am 22 years old and I know python, Typescript and Go.

# The agent must: detect which tool to call; extract name, age, skills; execute the correct python function; return structured JSON



def extract_name(text: str):
    import re
    match = re.search(r"My name is ([A-Za-z])", text)
    return match.group(1).strip() if match else "Unknown"

def extract_age(text: str):
    import re
    match = re.search(r"(\d+)", text)
    return int(match.group(1)) if match else None

def extract_skills(text: str):
    import re
    match = re.search(r"know (.+)", text)
    if match:
        skills = match.group(1).replace(".", "").split(",")
        return [s.strip() for s in skills]
    return []

tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_name",
            "description": "Extract the person's name from text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_age",
            "description": "Extract the person's age from text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_skills",
            "description": "Extract the person's skills from text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    }
]


from openai import OpenAI
import os, json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def info_agent(user_text: str):
    
    # 1: First LLM call
    first = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": 
                "You are an information extraction agent. "
                "When needed, call a tool to extract name, age, or skills."
            },
            {"role": "user", "content": user_text}
        ],
        tools=tools
    )
    
    msg = first.choices[0].message

    # 2: Check if LLM wants a tool
    if msg.tool_calls:

        tool_call = msg.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        # 3: Execute actual Python function
        if tool_name == "extract_name":
            result = extract_name(**args)
        elif tool_name == "extract_age":
            result = extract_age(**args)
        elif tool_name == "extract_skills":
            result = extract_skills(**args)
        else:
            result = "Unknown tool"
        
        # 4: Send tool result back to LLM
        final = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": 
                    "You are an info extraction agent. Use tools when needed."
                },
                {"role": "user", "content": user_text},
                msg,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            ]
        )
        return final.choices[0].message["content"]

    # If model didn't call a tool
    return msg["content"]


text = "My name is Aaryan Bajaj. I am 22 years old and I know Python, Go and TypeScript."

print(info_agent(text))