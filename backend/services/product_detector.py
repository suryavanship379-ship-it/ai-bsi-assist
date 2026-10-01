def detect_product(message):
    query = message.lower()

    products = {
        "stainless steel water bottles": [
            "stainless steel bottle",
            "stainless steel water bottle",
            "steel bottle",
            "water bottle"
        ],

        "helmets": [
            "helmet",
            "bike helmet",
            "motorcycle helmet",
            "two wheeler helmet"
        ],

        "cement": [
            "cement",
            "portland cement"
        ],

        "electrical switches": [
            "electrical switch",
            "electric switch",
            "switch"
        ],

        "pressure cookers": [
            "pressure cooker",
            "cooker"
        ],

        "toys": [
            "toy",
            "toys",
            "children toy",
            "kids toy"
        ],

        "packaged drinking water": [
            "packaged drinking water",
            "bottled water",
            "drinking water"
        ],

        "steel products": [
            "steel product",
            "steel products"
        ]
    }

    for product, keywords in products.items():
        for keyword in keywords:
            if keyword in query:
                return product

    return None