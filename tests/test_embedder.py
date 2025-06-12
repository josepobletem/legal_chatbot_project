# tests/test_embedder.py

import os
from app import embedder


def test_build_faiss_index():
    embedder.build_faiss_index()
    assert os.path.exists("app/vector_index/index.faiss")
    assert os.path.exists("app/vector_index/docs.pkl")
