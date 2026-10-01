from semantic_search import semantic_search


def build_context(result):
    """
    Convert retrieved BIS information into grounded context.
    """

    return f"""
Product: {result.get("product", "Unknown")}
Standard Number: {result.get("standard_number", "Not available")}
Standard Title: {result.get("standard_title", "Not available")}
Description: {result.get("description", "Not available")}
Certification Status: {result.get("certification_status", "Not available")}
Official Source: {result.get("source", "Bureau of Indian Standards")}
Source URL: {result.get("source_url", "Not available")}
Last Verified: {result.get("last_verified", "Not available")}
""".strip()


def retrieve_bis_context(user_query, top_k=3):
    """
    Retrieve relevant BIS records using semantic search.
    """

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
    """
    Create general compliance guidance.

    These are general workflow steps and do not invent
    product-specific testing requirements.
    """

    certification_status = result.get(
        "certification_status",
        "Not available"
    )

    return [
        "Identify the applicable Indian Standard.",
        f"Check the certification requirement: {certification_status}.",
        "Review the official BIS standard and applicable requirements.",
        "Check product-specific testing requirements from official BIS information.",
        "Identify an appropriate BIS-recognized laboratory where applicable.",
        "Prepare the required documents and certification application.",
        "Verify the latest requirements on the official BIS portal before proceeding."
    ]


def get_ai_response(user_query):
    """
    Main function for BIS Mitra AI/ML.

    This function is designed so that the Flask backend
    can call it later.
    """

    retrieval = retrieve_bis_context(user_query)

    # --------------------------------
    # No reliable match
    # --------------------------------

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
            "compliance_steps": [],
            "sources": []
        }

    # --------------------------------
    # Best semantic-search result
    # --------------------------------

    best_result = retrieval["results"][0]

    product = best_result.get("product")
    standard_number = best_result.get("standard_number")
    standard_title = best_result.get("standard_title")

    certification_status = best_result.get(
        "certification_status"
    )

    similarity_score = best_result.get(
        "similarity_score"
    )

    compliance_steps = create_compliance_steps(
        best_result
    )

    # --------------------------------
    # Grounded conversational response
    # --------------------------------

    reply = (
        f"For {product}, the most relevant Indian Standard "
        f"in the current BIS Mitra knowledge base is "
        f"{standard_number} - {standard_title}. "
        f"The recorded certification status is "
        f"{certification_status}. "
        f"Please verify the latest product-specific requirements "
        f"using the official BIS source before proceeding."
    )

    # --------------------------------
    # Structured response for backend
    # --------------------------------

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
            response["standard"][
                "certification_status"
            ]
        )

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