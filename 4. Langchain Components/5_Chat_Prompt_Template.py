from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

model= ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5
)


chat_history = [SystemMessage(content="You are a helpful assistant.")
            ]

chat_template = ChatPromptTemplate.from_messages([
    ('system', "you are a helpful {domain} assistant."),
    ('human', "Tell me about {topic} in very short sentences.")
])

prompt=chat_template.invoke({"domain":"Ai","topic":"langchain"})

print(f'Prompt: {prompt}')

# while True:
#     user_input = input('You: ')
#     chat_history.append(HumanMessage(content=user_input))
#     if(user_input.lower() == 'exit'):
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(AIMessage(content=result.content))
#     print(f'AI: {result.content}')

print("Chat session ended.- This is yor chat history:", chat_history)