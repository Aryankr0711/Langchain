from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm= OpenAI(model="gpt-4o-mini")

result= llm.invoke("Who is Prime Minister of India?")

print(result)