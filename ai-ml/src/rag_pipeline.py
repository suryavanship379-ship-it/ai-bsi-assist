from semantic_search import semantic_search


def build_context(result):
    """Convert retrieved BIS information into grounded context."""

    testing = result.get("testing_requirements", [])
    laboratory = result.get(
        "laboratory",
        "Not available"
    )

    testing_text = ", ".join(testing) if testing else "Not available"

    return f"""
Product: {result.get("product", "Unknown")}
Standard Number: {result.get("standard_number", "Not available")}
Standard Title: {result.get("standard_title", "Not available")}
Description: {result.get("description", "Not available")}
Certification Status: {result.get("certification_status", "Not available")}
Testing Requirements: {testing_text}
Laboratory: {laboratory}
Official Source: {result.get("source", "Bureau of Indian Standards")}
Source URL: {result.get("source_url", "Not available")}
Last Verified: {result.get("last_verified", "Not available")}
""".strip()


def retrieve_bis_context(user_query, top_k=3):
    """Retrieve relevant BIS records using semantic search."""

    results = semantic_search(
        user_query,
        top_k=top_k
    )

    if not results:
        return {
            "status": "no_match",
            "query": user_query,
            "results": [],
            "context": ""
        }

    contexts = [
        build_context(result)
        for result in results
    ]

    return {
        "status": "success",
        "query": user_query,
        "results": results,
        "context": "\n\n---\n\n".join(contexts)
    }


def create_compliance_steps(result):
    """Create general BIS compliance guidance."""

    certification_status = result.get(
        "certification_status",
        "Not available"
    )

    return [
        "Identify the applicable Indian Standard.",
        f"Check the certification requirement: {certification_status}.",
        "Review the official BIS standard and applicable requirements.",
        "Complete the applicable product testing.",
        "Identify an appropriate BIS-recognized laboratory where applicable.",
        "Prepare the required documents and certification application.",
        "Verify the latest requirements on the official BIS portal before proceeding."
    ]


def get_ai_response(user_query):

    retrieval = retrieve_bis_context(user_query)

    if retrieval["status"] == "no_match":

        return {
            "status": "no_match",
            "reply": (
                "I could not find a sufficiently reliable BIS "
                "standard for this product in the current "
                "knowledge base. Please verify the product using "
                "official BIS resources."
            ),
            "product": None,
            "standard": None,
            "testing_requirements": [],
            "laboratory": None,
            "compliance_steps": [],
            "sources": []
        }

    best_result = retrieval["results"][0]

    product = best_result.get("product")
    standard_number = best_result.get("standard_number")
    standard_title = best_result.get("standard_title")

    certification_status = best_result.get(
        "certification_status"
    )

    testing_requirements = best_result.get(
        "testing_requirements",
        []
    )

    laboratory = best_result.get(
        "laboratory",
        "Not available"
    )

    similarity_score = best_result.get(
        "similarity_score"
    )

    compliance_steps = create_compliance_steps(
        best_result
    )

    testing_text = (
        "; ".join(testing_requirements)
        if testing_requirements
        else "Product-specific testing requirements should be verified from the official BIS standard."
    )

    reply = (
        f"For {product}, the most relevant Indian Standard "
        f"in the current BIS Mitra knowledge base is "
        f"{standard_number} - {standard_title}. "
        f"The recorded certification status is "
        f"{certification_status}. "
        f"Testing requirements available in the current "
        f"knowledge base include: {testing_text}. "
        f"The suggested laboratory category is: {laboratory}. "
        f"Please verify the latest product-specific requirements "
        f"using the official BIS source before proceeding."
    )

    return {
        "status": "success",

        "reply": reply,

        "product": product,

        "standard": {
            "number": standard_number,
            "title": standard_title,
            "certification_status": certification_status,
            "similarity_score": similarity_score
        },

        "testing_requirements": testing_requirements,

        "laboratory": laboratory,

        "compliance_steps": compliance_steps,

        "sources": [
            {
                "title": best_result.get(
                    "source",
                    "Bureau of Indian Standards"
                ),
                "url": best_result.get("source_url"),
                "last_verified": best_result.get(
                    "last_verified"
                )
            }
        ],

        "rag_context": retrieval["context"]
    }


if __name__ == "__main__":

    print("\n====================================")
    print("        BIS MITRA AI ASSISTANT")
    print("====================================")

    query = input("\nAsk your BIS question: ")

    response = get_ai_response(query)

    print("\n------------------------------------")
    print("ANSWER")
    print("------------------------------------")

    print(response["reply"])

    if response["status"] == "success":

        print("\nProduct:")
        print(response["product"])

        print("\nBIS Standard:")
        print(response["standard"]["number"])

        print("\nCertification Status:")
        print(
            response["standard"]["certification_status"]
        )

        print("\nTesting Requirements:")

        for test in response["testing_requirements"]:
            print(f"- {test}")

        print("\nLaboratory:")
        print(response["laboratory"])

        print("\nCompliance Journey:")

        for number, step in enumerate(
            response["compliance_steps"],
            start=1
        ):
            print(f"{number}. {step}")

        print("\nOfficial BIS Source:")

        for source in response["sources"]:
            print(source["title"])
            print(source["url"])

    print("\n====================================")