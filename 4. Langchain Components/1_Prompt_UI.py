from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("Researcher Tool")

user_prompt = st.text_input("Enter your prompt here:")

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5
)

if st.button("Sumarize"):
    result = model.invoke(user_prompt)
    st.write(result.content)




