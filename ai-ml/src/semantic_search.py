import json
import re
from pathlib import Path

import faiss
import numpy as np

from embedding_model import create_embedding


BASE_DIR = Path(__file__).resolve().parent.parent

INDEX_PATH = BASE_DIR / "vector_db" / "bis_index.faiss"
METADATA_PATH = BASE_DIR / "vector_db" / "bis_metadata.json"


def load_vector_database():
    """
    Load the FAISS vector index and BIS metadata.
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


def normalize_text(text):
    """
    Convert text to lowercase words for simple product matching.
    """

    text = str(text).lower()
    return set(re.findall(r"[a-z0-9]+", text))


def has_product_evidence(query, record):
    """
    Check whether the query shares meaningful words with the
    product name or one of its aliases.
    """

    query_words = normalize_text(query)

    product_texts = [record.get("product", "")]

    aliases = record.get("aliases", [])

    if isinstance(aliases, list):
        product_texts.extend(aliases)

    # Very common words should not count as product evidence.
    ignored_words = {
        "i", "a", "an", "the", "for", "of", "and", "or",
        "to", "in", "with", "which", "what", "is", "are",
        "want", "start", "sell", "make", "manufacture",
        "manufacturer", "business", "product", "standard",
        "bis", "indian", "applies", "applicable"
    }

    query_words = query_words - ignored_words

    for text in product_texts:
        product_words = normalize_text(text) - ignored_words

        if query_words.intersection(product_words):
            return True

    return False


def semantic_search(
    query,
    top_k=3,
    min_score=0.30,
    strong_score=0.45
):
    """
    Search BIS records using semantic similarity.

    Rules:
    1. Reject results below min_score.
    2. Accept very strong semantic matches automatically.
    3. For borderline matches, require product/alias evidence.
    """

    index, metadata = load_vector_database()

    if index.ntotal == 0:
        return []

    query_embedding = create_embedding(query)

    query_embedding = np.asarray(
        [query_embedding],
        dtype="float32"
    )

    # Search a few extra candidates before filtering.
    search_k = min(
        max(top_k * 3, top_k),
        index.ntotal
    )

    scores, indices = index.search(
        query_embedding,
        search_k
    )

    results = []

    for score, index_position in zip(
        scores[0],
        indices[0]
    ):

        if index_position == -1:
            continue

        score = float(score)

        # Too weak semantically
        if score < min_score:
            continue

        record = metadata[index_position].copy()

        product_evidence = has_product_evidence(
            query,
            record
        )

        # Borderline semantic matches need product evidence.
        if score < strong_score and not product_evidence:
            continue

        record["similarity_score"] = round(
            score,
            4
        )

        record["product_evidence"] = product_evidence

        results.append(record)

        if len(results) >= top_k:
            break

    return results


if __name__ == "__main__":

    print("\nBIS Mitra - Semantic Search")
    print("--------------------------")

    user_query = input(
        "Enter your product/query: "
    )

    results = semantic_search(user_query)

    if not results:

        print("\nNo matching BIS records found.")

        print(
            "The system could not find a sufficiently "
            "reliable BIS standard for this query."
        )

    else:

        print("\nRecommended BIS Standard(s):")

        for number, result in enumerate(
            results,
            start=1
        ):

            print(f"\nResult {number}")

            print(
                "Product:",
                result.get("product")
            )

            print(
                "Standard:",
                result.get("standard_number")
            )

            print(
                "Title:",
                result.get("standard_title")
            )

            print(
                "Certification:",
                result.get("certification_status")
            )

            print(
                "Similarity Score:",
                result.get("similarity_score")
            )

            print(
                "Product Evidence:",
                result.get("product_evidence")
            )

            print(
                "Source:",
                result.get("source")
            )