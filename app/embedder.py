# app/embedder.py

import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from typing import List

EMBEDDINGS_PATH = "app/vector_index"
DOCS_PATH = "app/docs"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents() -> List[str]:
    docs = []
    for filename in os.listdir(DOCS_PATH):
        filepath = os.path.join(DOCS_PATH, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs


def build_faiss_index():
    docs = load_documents()
    embeddings = model.encode(docs, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(EMBEDDINGS_PATH, exist_ok=True)
    faiss.write_index(index, os.path.join(EMBEDDINGS_PATH, "index.faiss"))
    with open(os.path.join(EMBEDDINGS_PATH, "docs.pkl"), "wb") as f:
        pickle.dump(docs, f)

    print(f"Índice FAISS creado con {len(docs)} documentos.")
