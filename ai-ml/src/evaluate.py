import json
from pathlib import Path

from semantic_search import semantic_search


BASE_DIR = Path(__file__).resolve().parent.parent
EVALUATION_FILE = BASE_DIR / "data" / "evaluation_queries.json"


def load_evaluation_data():
    """
    Load evaluation queries and expected BIS standards.
    expected_standard = None means that no match is expected
    from the current knowledge base.
    """
    with open(EVALUATION_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate():
    """
    Evaluate:
    1. Top-1 recommendation accuracy
    2. Top-3 recommendation accuracy
    3. Unsupported-query rejection accuracy
    """

    evaluation_data = load_evaluation_data()

    total_queries = len(evaluation_data)

    top1_correct = 0
    top3_correct = 0

    supported_total = 0
    supported_top1_correct = 0
    supported_top3_correct = 0

    unsupported_total = 0
    rejected_correctly = 0

    print("\nBIS Mitra - Semantic Search Evaluation")
    print("--------------------------------------")

    for number, item in enumerate(evaluation_data, start=1):

        query = item["query"]
        expected_standard = item["expected_standard"]

        results = semantic_search(
            query,
            top_k=3
        )

        predicted_standards = [
            result.get("standard_number")
            for result in results
        ]

        if predicted_standards:
            top1_prediction = predicted_standards[0]
        else:
            top1_prediction = None

        # ---------------------------------
        # Unsupported query
        # ---------------------------------

        if expected_standard is None:

            unsupported_total += 1

            rejected = len(predicted_standards) == 0

            if rejected:
                rejected_correctly += 1
                top1_correct += 1
                top3_correct += 1
                status = "CORRECTLY REJECTED"
            else:
                status = "WRONG - FALSE MATCH"

            print(f"\nTest {number}")
            print(f"Query: {query}")
            print("Expected: NO MATCH")

            if top1_prediction is None:
                print("Top-1 Prediction: NO MATCH")
            else:
                print(
                    f"Top-1 Prediction: {top1_prediction}"
                )

            if predicted_standards:
                print(
                    "Returned Standards:",
                    ", ".join(predicted_standards)
                )
            else:
                print("Returned Standards: NO MATCH")

            print(f"Result: {status}")

        # ---------------------------------
        # Supported query
        # ---------------------------------

        else:

            supported_total += 1

            top1_match = (
                top1_prediction == expected_standard
            )

            top3_match = (
                expected_standard in predicted_standards
            )

            if top1_match:
                top1_correct += 1
                supported_top1_correct += 1

            if top3_match:
                top3_correct += 1
                supported_top3_correct += 1

            print(f"\nTest {number}")
            print(f"Query: {query}")
            print(f"Expected: {expected_standard}")

            if top1_prediction is None:
                print("Top-1 Prediction: NO MATCH")
            else:
                print(
                    f"Top-1 Prediction: {top1_prediction}"
                )

            if predicted_standards:
                print(
                    "Top-3 Predictions:",
                    ", ".join(predicted_standards)
                )
            else:
                print("Top-3 Predictions: NO MATCH")

            print(
                "Top-1 Result:",
                "CORRECT" if top1_match else "WRONG"
            )

            print(
                "Top-3 Result:",
                "CORRECT" if top3_match else "WRONG"
            )

    # ---------------------------------
    # Calculate metrics
    # ---------------------------------

    overall_top1_accuracy = (
        (top1_correct / total_queries) * 100
        if total_queries
        else 0
    )

    overall_top3_accuracy = (
        (top3_correct / total_queries) * 100
        if total_queries
        else 0
    )

    supported_top1_accuracy = (
        (supported_top1_correct / supported_total) * 100
        if supported_total
        else 0
    )

    supported_top3_accuracy = (
        (supported_top3_correct / supported_total) * 100
        if supported_total
        else 0
    )

    rejection_accuracy = (
        (rejected_correctly / unsupported_total) * 100
        if unsupported_total
        else 0
    )

    # ---------------------------------
    # Summary
    # ---------------------------------

    print("\n======================================")
    print("EVALUATION SUMMARY")
    print("======================================")

    print(f"Total queries: {total_queries}")

    print(f"\nSupported queries: {supported_total}")
    print(
        f"Supported Top-1 Accuracy: "
        f"{supported_top1_accuracy:.2f}%"
    )
    print(
        f"Supported Top-3 Accuracy: "
        f"{supported_top3_accuracy:.2f}%"
    )

    print(f"\nUnsupported queries: {unsupported_total}")
    print(
        f"Correctly rejected: "
        f"{rejected_correctly}"
    )
    print(
        f"Rejection Accuracy: "
        f"{rejection_accuracy:.2f}%"
    )

    print("\nOverall Results")
    print(
        f"Overall Top-1 Accuracy: "
        f"{overall_top1_accuracy:.2f}%"
    )
    print(
        f"Overall Top-3 Accuracy: "
        f"{overall_top3_accuracy:.2f}%"
    )

    print("======================================")


if __name__ == "__main__":
    evaluate()