from langchain_huggingface import  HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

document = [
    "Deep space exploration missions require advanced autonomous navigation systems to calculate precise trajectories across distant galaxies without relying on real-time ground control communication.",
    "Ancient Mediterranean architecture heavily utilized subterranean limestone columns and complex aqueduct networks to sustain massive urban populations during prolonged summer droughts.",
    "Modern culinary arts frequently integrate chemical principles from molecular gastronomy to transform liquid ingredients into delicate textures like culinary foams and edible gels.",
    "Global financial markets are rapidly shifting toward decentralized blockchain protocols to execute automated high-frequency trading settlements without traditional institutional intermediaries.",
    "Marine biologists studying deep-sea hydrothermal vents have discovered unique extremophile organisms that thrive in toxic, high-pressure environments by utilizing chemosynthesis instead of photosynthesis."
]

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

Document_embeddings=embedding.embed_documents(document)

Query="What are the unique organisms found in deep-sea hydrothermal vents?"

Query_embedding=embedding.embed_query(Query)

# Calculate cosine similarity between the query embedding and document embeddings
similarity_scores = cosine_similarity([Query_embedding], Document_embeddings)

print("Similarity scores:", similarity_scores)

# Get the index of the most similar document
most_similar_index = np.argmax(similarity_scores)

print(f"The most similar document is at index: {most_similar_index}")
print(f"The most similar document is: {document[most_similar_index]}")

# Output:
# Similarity scores: [[0.11760738 0.19160537 0.09864033 0.0072289  0.74844981]]
# The most similar document is at index: 4
# The most similar document is: Marine biologists studying deep-sea hydrothermal vents have discovered unique extremophile organisms that thrive in toxic, high-pressure environments by utilizing chemosynthesis instead of photosynthesis.