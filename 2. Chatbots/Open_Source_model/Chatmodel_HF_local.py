from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    task="text-generation",
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    pipeline_kwargs={"temperature":1.5, "max_new_tokens":512}
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("write an poem on diwali")

print(result.content)
