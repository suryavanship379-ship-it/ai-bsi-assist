import json
from pathlib import Path


# Path to the AI/ML project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to BIS knowledge-base JSON file
KNOWLEDGE_BASE_PATH = BASE_DIR / "data" / "bis_knowledge_base.json"


def load_knowledge_base():
    """
    Load BIS product and standard information from the JSON knowledge base.
    """
    try:
        with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Knowledge base must contain a JSON list.")

        return data

    except FileNotFoundError:
        print(f"Knowledge base not found: {KNOWLEDGE_BASE_PATH}")
        return []

    except json.JSONDecodeError as error:
        print(f"Invalid JSON in knowledge base: {error}")
        return []


def create_search_text(record):
    """
    Combine useful fields into one searchable text.

    Later, Sentence Transformers will convert this text
    into an embedding vector.
    """
    product = record.get("product", "")
    aliases = " ".join(record.get("aliases", []))
    standard_number = record.get("standard_number", "")
    standard_title = record.get("standard_title", "")
    description = record.get("description", "")

    return (
        f"Product: {product}. "
        f"Aliases: {aliases}. "
        f"Standard: {standard_number}. "
        f"Standard title: {standard_title}. "
        f"Description: {description}."
    )


if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    print(f"Loaded {len(knowledge_base)} BIS record(s).")

    for record in knowledge_base:
        print("\nProduct:", record.get("product"))
        print("Standard:", record.get("standard_number"))
        print("Search text:", create_search_text(record))