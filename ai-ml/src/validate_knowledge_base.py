import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "bis_knowledge_base.json"


REQUIRED_FIELDS = [
    "product",
    "aliases",
    "standard_number",
    "standard_title",
    "description",
    "certification_status",
    "source",
    "source_url",
    "last_verified"
]


def validate_date(date_string):
    """
    Check whether last_verified uses YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def validate_knowledge_base():

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)

    except FileNotFoundError:
        print("ERROR: Knowledge-base file was not found.")
        return

    except json.JSONDecodeError as error:
        print("ERROR: Invalid JSON.")
        print(error)
        return

    if not isinstance(records, list):
        print("ERROR: Knowledge base must contain a JSON list.")
        return

    print("\nBIS Knowledge Base Validation")
    print("-----------------------------")
    print(f"Total BIS records: {len(records)}")

    errors = 0

    for number, record in enumerate(records, start=1):

        print(f"\nChecking record {number}...")

        # Check required fields
        missing_fields = [
            field
            for field in REQUIRED_FIELDS
            if field not in record
        ]

        if missing_fields:
            errors += 1

            print(
                "Missing fields:",
                ", ".join(missing_fields)
            )

        # Check aliases
        if "aliases" in record:

            if not isinstance(record["aliases"], list):
                errors += 1
                print("ERROR: aliases must be a list.")

        # Check source URL
        if "source_url" in record:

            source_url = record["source_url"]

            if not source_url.startswith("https://"):
                errors += 1
                print(
                    "ERROR: source_url must start with https://"
                )

        # Check verification date
        if "last_verified" in record:

            if not validate_date(record["last_verified"]):
                errors += 1

                print(
                    "ERROR: last_verified must use "
                    "YYYY-MM-DD format."
                )

    print("\n================================")

    if errors == 0:
        print("Knowledge base structure is valid.")
    else:
        print(f"Validation found {errors} problem(s).")

    print("================================")


if __name__ == "__main__":
    validate_knowledge_base()