from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model= OpenAIEmbeddings(model="text-embedding-3-large")

result= model.embed_query("What is the capital of India?")

print(result)