import os
from app import embedder

DOCS_DIR: str = "app/docs"
DOC_FILE: str = os.path.join(DOCS_DIR, "ejemplo_despido.txt")


def init_test_docs() -> None:
    """
    Inicializa un archivo de prueba legal en app/docs/.

    Esta función crea el directorio `app/docs/` si no existe
    y luego genera un archivo `ejemplo_despido.txt` con contenido
    legal simulado para pruebas de embeddings.

    Returns
    -------
    None
    """
    os.makedirs(DOCS_DIR, exist_ok=True)

    if not os.path.exists(DOC_FILE):
        with open(DOC_FILE, "w", encoding="utf-8") as f:
            f.write(
                "Artículo 161 del Código del Trabajo chileno establece que el empleador "
                "puede poner término al contrato de trabajo por necesidades de la empresa, "
                "tales como bajas en productividad, cambios en el mercado o innovación tecnológica.\n\n"
                "El trabajador tiene derecho a una indemnización equivalente a 30 días por cada año "
                "de servicio con un máximo de 330 días, salvo pacto diferente."
            )


def test_build_faiss_index() -> None:
    """
    Testea que el índice FAISS se construya correctamente desde documentos legales.

    Llama a `embedder.build_faiss_index()` después de preparar un documento
    simulado. Verifica que se generen los archivos `index.faiss` y `docs.pkl`.

    Returns
    -------
    None
    """
    init_test_docs()
    embedder.build_faiss_index()

    assert os.path.exists("app/vector_index/index.faiss")
    assert os.path.exists("app/vector_index/docs.pkl")
