
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    timeout=30,
    max_retries=1
)

print("Sending request to Gemini...")

try:
    result = model.invoke("Write a short poem on diwali")
    print(result.text)

except Exception as e:
    print("Error:", e)
