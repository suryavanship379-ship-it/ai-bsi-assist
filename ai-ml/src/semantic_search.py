import json
from pathlib import Path

import faiss
import numpy as np

from embedding_model import create_embedding


BASE_DIR = Path(__file__).resolve().parent.parent

INDEX_PATH = BASE_DIR / "vector_db" / "bis_index.faiss"
METADATA_PATH = BASE_DIR / "vector_db" / "bis_metadata.json"


def load_vector_database():
    """
    Load the FAISS vector index and its corresponding BIS metadata.
    """

    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            "FAISS index not found. Run build_vector_index.py first."
        )

    if not METADATA_PATH.exists():
        raise FileNotFoundError(
            "BIS metadata not found. Run build_vector_index.py first."
        )

    index = faiss.read_index(str(INDEX_PATH))

    with open(METADATA_PATH, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    return index, metadata


def semantic_search(query, top_k=3, min_score=0.30):
    """
    Search for BIS records that are semantically similar
    to the user's query.

    Results below the minimum similarity score are ignored.
    """

    index, metadata = load_vector_database()

    if index.ntotal == 0:
        return []

    # Convert user query into an embedding
    query_embedding = create_embedding(query)

    query_embedding = np.asarray(
        [query_embedding],
        dtype="float32"
    )

    # Don't request more results than available records
    k = min(top_k, index.ntotal)

    # Search FAISS
    scores, indices = index.search(query_embedding, k)

    results = []

    for score, index_position in zip(scores[0], indices[0]):

        # Ignore invalid FAISS results
        if index_position == -1:
            continue

        # Ignore results with low semantic similarity
        if float(score) < min_score:
            continue

        record = metadata[index_position].copy()

        record["similarity_score"] = round(float(score), 4)

        results.append(record)

    return results


if __name__ == "__main__":

    print("\nBIS Mitra - Semantic Search")
    print("--------------------------")

    user_query = input("Enter your product/query: ")

    results = semantic_search(user_query)

    if not results:
        print("\nNo matching BIS records found.")
        print(
            "The system could not find a sufficiently reliable "
            "BIS standard for this query."
        )

    else:
        print("\nRecommended BIS Standard(s):")

        for number, result in enumerate(results, start=1):

            print(f"\nResult {number}")
            print("Product:", result.get("product"))
            print("Standard:", result.get("standard_number"))
            print("Title:", result.get("standard_title"))
            print(
                "Certification:",
                result.get("certification_status")
            )
            print(
                "Similarity Score:",
                result.get("similarity_score")
            )
            print("Source:", result.get("source"))