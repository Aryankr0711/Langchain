from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5
)

result = model.invoke("write a professional email to request a holiday on diwali")

print(result.content)