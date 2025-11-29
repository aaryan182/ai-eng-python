
def extract_name(text):
    import re
    m = re.search(r"[A-Z][a-z]+(?: [A-Z][a-z]+)*", text)
    return m.group(0)

def extract_age(text):
    import re
    m = re.search(r"\b(\d{1,2})\b", text)
    return int(m.group(1))

def extract_skills(text):
    import re
    if "know" in text.lower():
        part = text.split("know")[1]
        skills = part.replace(".", "").split(",")
        return [s.strip() for s in skills]
    return []

def extract_domain(text):
    if "ai" in text.lower():
        return "Artificial Intelligence"
    return "Unknown"


# TOOL SCHEMAS

tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_name",
            "description": "Extract user's name.",
            "parameters": {"type": "object","properties":{"text":{"type":"string"}},"required":["text"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_age",
            "description": "Extract user's age.",
            "parameters": {"type": "object","properties":{"text":{"type":"string"}},"required":["text"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_skills",
            "description": "Extract user's skills.",
            "parameters": {"type": "object","properties":{"text":{"type":"string"}},"required":["text"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_domain",
            "description": "Extract user's career domain.",
            "parameters": {"type": "object","properties":{"text":{"type":"string"}},"required":["text"]}
        }
    }
]

# STEP 1 — EXTRACTION AGENT (ReAct Loop Agent)

# This agent will:

# Think

# Choose tool

# Use tool

# Store results in state

# Repeat until all fields are found


from openai import OpenAI
import json

client = OpenAI()

def extraction_agent(text):
    state = {"name": str, "age": None, "skills": None, "domain": None}
    
    memory = [
        {
            "role": "system", "content":
            "You are an intelligent extraction agent"
            "Use tools to extract name, age, skills, domain"
            "When a field is already extracted, do no extract again."
        },
        {"role": "user", "content": text}
    ]

    for step in range(8):
        print(f"\n Step {step +1}")
    
        response = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = memory,
            tools = tools
        )
        
        msg = response.choices[0].message
        memory.append(msg)
        
        if not msg.tool_calls:
            print("Agent ended with final answer")
            break
        
        tool_call = msg.tool_calls[0]
        fn = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        #execute tool
        if fn == "extract_name":
            state["name"] = extract_name(**args)
            result = state["name"]
            
        elif fn == "extract_age":
            state['age'] = extract_age(**args)
            result = state["age"]
        
        elif fn == "extract_skills":
            state["skills"] = extract_skills(**args)
            result = state['skills']
            
        elif fn == "extract_domain":
            state['domain'] = extract_domain(**args)
            result = state['domain']
            
        # Add tool result back as observation
        
        memory.append({
            "role":"tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })
        
        print(f"State Updated: {state}")
        
        if all(state.values()):
            print("All fields extracted, stopping early")
            break
    
    return state


# Step 2 - Validation agent ( Fix missing or wrong data)
# This agent uses the LLM to check and fix issues 


def validation_agent(state, text):
    prompt = f"""
You are a validation agent.

Given the extracted state:

{json.dumps(state, indent=2)}

And the original text:
{text}

Correct missing or incorrect fields.
Return ONLY valid JSON.
"""

    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message["content"])


# Step - 3 Final Formatting Agent 

def final_agent(state):
    prompt = f"""
    Format this state into clean JSON:
    {json.dumps(state, indent= 2)}
    
    Ensure: 
    - name is string
    - age is number
    - skills is array of strings
    - domain is string
    
    """
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [{
            "role": "user", "content": prompt
        }]
        
        return json.loads(response.choices[0].message["content"])
    )
    
    return json.loads(response.choices[0].message["content"])

# Step 4 - full pipeline

def upgraded_day10_agent(text):
    print("\n🚀 STARTING EXTRACTION PHASE")
    state = extraction_agent(text)

    print("\n🔍 VALIDATING DATA")
    state = validation_agent(state, text)

    print("\n🎨 FORMATTING FINAL OUTPUT")
    final = final_agent(state)

    print("\n✅ PIPELINE DONE")
    return final

text = "My name is Aaryan Bajaj and I am 22. I know Python, Go, and TypeScript. I work in AI."

print(upgraded_day10_agent(text))


# OUTPUT (Perfect Clean JSON)
# {
#   "name": "Aaryan Bajaj",
#   "age": 22,
#   "skills": ["Python", "Go", "TypeScript"],
#   "domain": "Artificial Intelligence"
# }