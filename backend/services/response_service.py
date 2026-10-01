from services.intent_detector import detect_intent


def standard_card(product):
    return {
        "type": "standard",
        "data": {
            "title": "Applicable Indian Standard",
            "product": product or "Product not identified",
            "description": (
                "The applicable Indian Standard will be identified "
                "from official BIS information based on the exact "
                "product, material and intended use."
            ),
            "standardNumber": None,
            "verified": False
        }
    }


def certification_card(product):
    return {
        "type": "certification",
        "data": {
            "title": "BIS Certification",
            "product": product or "Product not identified",
            "description": (
                "Certification requirements depend on the product, "
                "applicable Indian Standard and relevant BIS scheme."
            ),
            "status": "To be verified"
        }
    }


def testing_card(product):
    return {
        "type": "testing",
        "data": {
            "title": "Testing Requirements",
            "product": product or "Product not identified",
            "description": (
                "Testing requirements should be determined from "
                "the applicable Indian Standard and BIS scheme."
            ),
            "tests": []
        }
    }


def laboratory_card(product):
    return {
        "type": "lab",
        "data": {
            "title": "Laboratory / Testing Facility",
            "product": product or "Product not identified",
            "description": (
                "The appropriate laboratory depends on the required "
                "tests and applicable product standard."
            ),
            "location": "To be identified"
        }
    }


def journey_card(product):
    return {
        "type": "journey",
        "data": {
            "title": "BIS Compliance Journey",
            "product": product or "Your product",
            "steps": [
                "Identify the product",
                "Identify applicable Indian Standard",
                "Check applicable BIS scheme",
                "Review requirements",
                "Arrange product testing",
                "Prepare required documents",
                "Submit relevant application",
                "Complete applicable assessment",
                "Confirm certification or licence status",
                "Maintain compliance"
            ]
        }
    }


def get_previous_product(conversation_history):
    """
    Finds a product mentioned earlier in the conversation.
    This prepares the API for contextual follow-up questions.
    """

    if not conversation_history:
        return None

    product_keywords = {
        "stainless steel water bottles": [
            "stainless steel bottle",
            "stainless steel water bottle",
            "steel bottle",
            "water bottle"
        ],
        "helmets": ["helmet"],
        "cement": ["cement"],
        "electrical switches": ["electrical switch", "electric switch"],
        "pressure cookers": ["pressure cooker"],
        "toys": ["toy", "toys"],
        "packaged drinking water": [
            "packaged drinking water",
            "bottled water"
        ]
    }

    for item in reversed(conversation_history):

        if item.get("role") != "user":
            continue

        content = item.get("content", "").lower()

        for product, keywords in product_keywords.items():
            for keyword in keywords:
                if keyword in content:
                    return product

    return None


def generate_response(message, product=None, conversation_history=None):

    if conversation_history is None:
        conversation_history = []

    query = message.lower()

    # Use previous product for follow-up questions
    if product is None:
        product = get_previous_product(conversation_history)

    intent = detect_intent(message)

    # Greeting
    if intent == "greeting":
        return {
            "text": (
                "Hello! 👋 I'm BIS Mitra, your AI guide to Indian "
                "Standards and BIS services. Tell me about your "
                "product or ask about standards, certification, "
                "testing or laboratories."
            ),
            "cards": [],
            "sources": []
        }

    # BIS information
    if intent == "bis":
        return {
            "text": (
                "BIS stands for the Bureau of Indian Standards. "
                "It is India's National Standards Body. BIS develops "
                "Indian Standards and provides services related to "
                "product certification, testing, laboratories, "
                "hallmarking and consumer-related activities."
            ),
            "cards": [],
            "sources": []
        }

    # Product not known
    if not product:
        return {
            "text": (
                "I'd be happy to help. Tell me the product you are "
                "manufacturing or planning to manufacture. For example:\n\n"
                "\"I want to manufacture stainless steel water bottles.\""
            ),
            "cards": [],
            "sources": []
        }

    # Standard
    if intent == "standard":
        return {
            "text": (
                f"For **{product}**, the first step is to identify "
                "the applicable Indian Standard. The exact standard "
                "depends on the product type, material and intended use. "
                "The verified standard will be retrieved from the BIS "
                "knowledge base when the AI/RAG module is connected."
            ),
            "cards": [standard_card(product)],
            "sources": []
        }

    # Certification
    if intent == "certification":
        return {
            "text": (
                f"For **{product}**, BIS certification requirements "
                "depend on the applicable Indian Standard and relevant "
                "conformity assessment scheme. The exact requirements "
                "must be verified from current official BIS information."
            ),
            "cards": [
                standard_card(product),
                certification_card(product),
                journey_card(product)
            ],
            "sources": []
        }

    # Testing
    if intent == "testing":
        return {
            "text": (
                f"For **{product}**, testing requirements should be "
                "identified from the applicable Indian Standard and "
                "relevant BIS scheme. After identifying the tests, "
                "an appropriate laboratory can be selected."
            ),
            "cards": [
                standard_card(product),
                testing_card(product),
                laboratory_card(product)
            ],
            "sources": []
        }

    # Laboratory
    if intent == "laboratory":
        return {
            "text": (
                f"For **{product}**, the appropriate laboratory depends "
                "on the required tests and applicable standard. The "
                "laboratory scope should be verified before testing."
            ),
            "cards": [
                laboratory_card(product),
                testing_card(product)
            ],
            "sources": []
        }

    # Documents
    if intent == "documents":
        return {
            "text": (
                f"For **{product}**, required documents depend on the "
                "applicable BIS certification or conformity assessment "
                "scheme. The final document checklist should come from "
                "the relevant official BIS guidance."
            ),
            "cards": [
                certification_card(product),
                journey_card(product)
            ],
            "sources": []
        }

    # Journey
    if intent == "journey":
        return {
            "text": (
                f"Here is the general BIS compliance journey for "
                f"**{product}**. The exact steps depend on the applicable "
                "standard and BIS scheme."
            ),
            "cards": [journey_card(product)],
            "sources": []
        }

    # General product question
    return {
        "text": (
            f"Got it! You're working with **{product}**.\n\n"
            "I can help you explore the applicable Indian Standard, "
            "BIS certification, testing requirements, laboratories "
            "and compliance journey."
        ),
        "cards": [
            standard_card(product),
            certification_card(product),
            testing_card(product),
            laboratory_card(product),
            journey_card(product)
        ],
        "sources": []
    }