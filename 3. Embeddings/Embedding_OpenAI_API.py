from langchain_openai import EmbeddingOpenAI
from dotenv import load_dotenv

load_dotenv()

model= EmbeddingOpenAI(model="text-embedding-3-large")

result= model.invoke("What is the capital of India?")

print(result)