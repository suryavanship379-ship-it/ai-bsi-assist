from sentence_transformers import SentenceTransformer


# Lightweight and good for semantic similarity.
MODEL_NAME = "all-MiniLM-L6-v2"

_model = None


def get_embedding_model():
    """
    Load the Sentence Transformer model.

    The model is loaded only once and reused.
    """
    global _model

    if _model is None:
        print(f"Loading embedding model: {MODEL_NAME}")
        _model = SentenceTransformer(MODEL_NAME)

    return _model


def create_embedding(text):
    """
    Convert one piece of text into a numerical embedding vector.
    """
    model = get_embedding_model()

    embedding = model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding


def create_embeddings(texts):
    """
    Convert multiple texts into embedding vectors.
    """
    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings


if __name__ == "__main__":

    test_text = "I manufacture bottled drinking water"

    embedding = create_embedding(test_text)

    print("\nInput text:")
    print(test_text)

    print("\nEmbedding shape:")
    print(embedding.shape)

    print("\nFirst 10 values:")
    print(embedding[:10])
    