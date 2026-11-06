from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

chatbot= ChatOpenAI(model="gpt-4o-mini")

result= chatbot.invoke("Who is Prime Minister of India?")

print(result.content)