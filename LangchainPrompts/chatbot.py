from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
model = ChatOpenAI(api_key=api_key, 
                   base_url="https://openrouter.ai/api/v1",
                   model='openai/gpt-4o-mini')
chat_history = [SystemMessage(content="You are a helpful assistant.")]
while True:
    user_input = input("ME: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Chatbot Response:", result.content)
print("Chat history:", chat_history)