from langchain_huggingface import  HuggingFaceEmbeddings
import numpy as np

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document=["What is the capital of India?", 
          "India is a beautiful country with a rich cultural heritage.",
          "The Taj Mahal is one of the most famous landmarks in India."
    ]

result=embedding.embed_documents(document)
result_np = np.array(result)

print((result_np.shape))