# A decorator that logs: function name timestamp prompt response execution time

import time
from functools import wraps

def llm_logger(func):
    @wraps(func)
    def wrapper(prompt):
        print("LLm call start")
        print("Function:", func.__name__)
        print("Prompt:", prompt)
        start = time.time()
        
        result = func(prompt)
        
        end = time.time()
        print("Response:", result)
        print("Time:", round(end - start, 3), "sec")
        print("LLm call end")
        
        return result
    return wrapper


@llm_logger
def fake_llm(prompt):
    return prompt.upper()

fake_llm("hello agent")