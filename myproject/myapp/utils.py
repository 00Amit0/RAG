import faiss # type: ignore
import numpy as np # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Initialize the FAISS index
dimension = 384  # Dimension of the sentence transformer embeddings
index = faiss.IndexFlatL2(dimension)

# Store descriptions and their corresponding IDs
descriptions = []
ids = []

def add_to_index(description, id):
    embedding = model.encode([description])[0]
    index.add(np.array([embedding], dtype=np.float32))
    descriptions.append(description)
    ids.append(id)

def search_index(query, top_k=5):
    query_embedding = model.encode([query])[0]
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    results = [(ids[idx], descriptions[idx], distances[0][i]) for i, idx in enumerate(indices[0]) if idx != -1]
    return results
