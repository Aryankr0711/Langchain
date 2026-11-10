from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model= ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about langchain in very short sentences.")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(f'AI: {messages[-1].content}')