from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model="claude-3.0")

result= model.invoke("Who is Prime Minister of India?")

print(result.content)
