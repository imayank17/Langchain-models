from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
model = ChatOpenAI(api_key=api_key, 
                   base_url="https://openrouter.ai/api/v1",
                   model='openai/gpt-4o-mini')

while True:
    user_input = input("ME: ")
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(user_input)
    print("Chatbot Response:", result.content)