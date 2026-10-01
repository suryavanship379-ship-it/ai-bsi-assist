import json
from pathlib import Path

import faiss
import numpy as np

from knowledge_base import load_knowledge_base, create_search_text
from embedding_model import create_embeddings


BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_DB_DIR = BASE_DIR / "vector_db"

INDEX_PATH = VECTOR_DB_DIR / "bis_index.faiss"
METADATA_PATH = VECTOR_DB_DIR / "bis_metadata.json"


def build_vector_index():
    """
    Create embeddings for BIS knowledge-base records
    and store them in a FAISS vector index.
    """

    # Load BIS knowledge base
    knowledge_base = load_knowledge_base()

    if not knowledge_base:
        print("Knowledge base is empty.")
        return

    print(f"Loaded {len(knowledge_base)} BIS record(s).")

    # Prepare searchable text
    search_texts = [
        create_search_text(record)
        for record in knowledge_base
    ]

    print("Creating embeddings...")

    # Convert BIS records into embeddings
    embeddings = create_embeddings(search_texts)

    # FAISS requires float32
    embeddings = np.asarray(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    print(f"Embedding dimension: {dimension}")

    # Inner product works as cosine similarity because
    # our embeddings are normalized.
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    # Make sure vector_db exists
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, str(INDEX_PATH))

    # Save corresponding BIS metadata
    with open(METADATA_PATH, "w", encoding="utf-8") as file:
        json.dump(
            knowledge_base,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("\nFAISS index created successfully.")
    print(f"Total vectors stored: {index.ntotal}")
    print(f"Index saved to: {INDEX_PATH}")
    print(f"Metadata saved to: {METADATA_PATH}")


if __name__ == "__main__":
    build_vector_index()