# User gives:

# "Aaryan is 22. He knows Python and Go and works in AI."

# Agent must:

# Extract name

# Extract age

# Extract skills

# Extract domain

# Return final result

# LLM will decide the order.



# Define Tool Functions


def extract_name(text):
    import re
    m = re.search(r"[A-Z][a-z]+", text)
    return m.group(0) if m else "Unknown"

def extract_age(text):
    import re
    m = re.search(r"\b(\d{1,2})\b", text)
    return int(m.group(1)) if m else None

def extract_skills(text):
    if "knows" in text:
        return text.split("knows")[1].replace(".", "").split(",")
    return []

def extract_domain(text):
    if "AI" in text.upper():
        return "Artificial Intelligence"
    return "Unknown"


# Define Tools (Schemas)



tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_name",
            "description": "Extract name",
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_age",
            "description": "Extract age",
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_skills",
            "description": "Extract skills",
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_domain",
            "description": "Find career domain",
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"]
            }
        }
    },
]




# The Multi-Step Agent Loop


from openai import OpenAI
import os, json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def multi_agent(text):

    memory = [
        {"role": "system", "content": 
         "You are an intelligent multi-step agent. "
         "Think step-by-step, call tools as needed. "
         "When done, return a structured JSON with name, age, skills, domain."}
    ]

    memory.append({"role": "user", "content": text})

    extracted = {
        "name": None,
        "age": None,
        "skills": None,
        "domain": None
    }

    for _ in range(5):  # Max 5 steps
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=memory,
            tools=tools
        )

        msg = response.choices[0].message
        memory.append(msg)

        # If final output (no tool call)
        if not msg.tool_calls:
            return msg["content"]

        tool_call = msg.tool_calls[0]
        fn = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        # Execute tool
        if fn == "extract_name":
            extracted["name"] = extract_name(**args)
            tool_result = extracted["name"]

        elif fn == "extract_age":
            extracted["age"] = extract_age(**args)
            tool_result = extracted["age"]

        elif fn == "extract_skills":
            extracted["skills"] = extract_skills(**args)
            tool_result = extracted["skills"]

        elif fn == "extract_domain":
            extracted["domain"] = extract_domain(**args)
            tool_result = extracted["domain"]

        memory.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(tool_result)
        })

    return extracted


# Run the Agent

text = "Aaryan is 22. He knows Python, Go, AI and works in AI."
print(multi_agent(text))



# OUTPUT


{
  "name": "Aaryan",
  "age": 22,
  "skills": ["Python", "Go", "AI"],
  "domain": "Artificial Intelligence"
}


# The agent:

# Thought about what to do

# Called the proper tool

# Updated its memory

# Checked missing info

# Repeated actions until done