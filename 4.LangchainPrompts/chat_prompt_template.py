from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
chat_template = ChatPromptTemplate([
   ('system', "you are a helful {domain} expert"),
   ('human', "explain {topic} in simple terms")
])

prompt = chat_template.invoke({'domain':'cricketExpert', 'topic':'the offside rule in cricket'})
print(prompt)