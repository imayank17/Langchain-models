from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("OPENROUTER_API_KEY")
model=ChatOpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1",model='openai/gpt-4o-mini')

class SentimentInput(TypedDict):
    summary: str
    sentiment: str

structured_input = model.with_structured_output(SentimentInput)
result = structured_input.invoke("Best Bollywood movie of the year. It was absolutely brilliant. I really enjoyed all of it, the acting, cinematography, writing, pace, suspense, comedy, gore, music, soundtrack and much more. Love original movies like this. More of this please! Ho, mainu lutt le gaya")
print(result)
