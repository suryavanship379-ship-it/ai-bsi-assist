from rag_pipeline import get_ai_response


def test_backend_integration():

    message = "I manufacture PVC electrical wires for house wiring"

    response = get_ai_response(message)

    print("\nBIS MITRA - BACKEND INTEGRATION TEST")
    print("------------------------------------")

    print("Status:", response["status"])
    print("Reply:", response["reply"])

    if response["status"] == "success":

        print("\nProduct:")
        print(response["product"])

        print("\nStandard:")
        print(response["standard"]["number"])

        print("\nCompliance Steps:")

        for step in response["compliance_steps"]:
            print("-", step)

        print("\nSources:")

        for source in response["sources"]:
            print("-", source["url"])


if __name__ == "__main__":
    test_backend_integration()