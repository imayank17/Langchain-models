from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1",model='openai/gpt-4o-mini')

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

