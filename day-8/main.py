from dotenv import load_dotenv
from openai import OpenAI
import os

# load_dotenv()
# # api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

# def ask_llm(prompt):
#     response = client.chat.completions.create(
#         model = "gpt-4.1-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message["content"]


# print(ask_llm("Explain python in 2 lines"))



app = FastAPI()
app.include_router(chat_router)


def create_summary_prompt(text):
    return f"""
        You are a professional summarizer. Summarize the following text in 3 bullet points:

        {text}
     """
     
