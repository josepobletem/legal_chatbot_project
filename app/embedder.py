"""
Embedder de documentos legales para recuperación aumentada por FAISS.
"""

import os
import pickle
from typing import List

import faiss
import numpy as np
from loguru import logger
from sentence_transformers import SentenceTransformer

EMBEDDINGS_PATH = "app/vector_index"
DOCS_PATH = "app/docs"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents() -> List[str]:
    """
    Carga documentos legales desde el directorio especificado.

    Returns
    -------
    List[str]
        Lista de contenidos de los documentos encontrados.
    """
    docs = []
    for filename in os.listdir(DOCS_PATH):
        filepath = os.path.join(DOCS_PATH, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs


def build_faiss_index() -> None:
    """
    Construye un índice vectorial FAISS a partir de documentos legales.

    Genera embeddings con SentenceTransformer y crea un índice FAISS
    para búsquedas semánticas rápidas. Guarda el índice en disco.

    Returns
    -------
    None
    """
    docs = load_documents()
    if not docs:
        logger.warning("No se encontraron documentos en el directorio '%s'.", DOCS_PATH)
        return

    # Conversión explícita a float32 para compatibilidad con FAISS
    embeddings = np.asarray(model.encode(docs, convert_to_numpy=True)).astype("float32")

    if embeddings is None or len(embeddings) == 0:
        logger.warning("No se pudieron generar embeddings.")
        return

    dim = embeddings.shape[1] if len(embeddings.shape) > 1 else 384
    index = faiss.IndexFlatL2(dim)

    # ✅ Ignoramos falso positivo de pylint para método .add()
    index.add(embeddings)  # pylint: disable=no-value-for-parameter

    os.makedirs(EMBEDDINGS_PATH, exist_ok=True)
    faiss.write_index(index, os.path.join(EMBEDDINGS_PATH, "index.faiss"))
    with open(os.path.join(EMBEDDINGS_PATH, "docs.pkl"), "wb") as f:
        pickle.dump(docs, f)

    logger.success("Índice FAISS creado con {} documentos.", len(docs))
