from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
model = ChatOpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1",model='openai/gpt-4o-mini')
messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print("Chatbot Response:", result.content)
print("Chat history:", messages)