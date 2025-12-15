from openai import OpenAI
client = OpenAI()

def call_llm(prompt, model= "gpt-4.1-mini"):
    response = client.chat.completions.create(
        model = model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]