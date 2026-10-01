from flask import Flask, jsonify, request
from flask_cors import CORS

from services.product_detector import detect_product
from services.intent_detector import detect_intent
from services.response_service import generate_response

app = Flask(__name__)
CORS(app)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "BIS Mitra backend is running"
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json() or {}

        message = data.get("message", "").strip()
        conversation_history = data.get("conversationHistory", [])

        if not message:
            return jsonify({
                "status": "error",
                "reply": "Please enter a message.",
                "cards": [],
                "sources": []
            }), 400

        product = detect_product(message)

        result = generate_response(
            message=message,
            product=product,
            conversation_history=conversation_history
        )

        return jsonify({
            "status": "success",
            "reply": result["text"],
            "cards": result.get("cards", []),
            "sources": result.get("sources", [])
        })

    except Exception as error:
        print("Chat error:", error)

        return jsonify({
            "status": "error",
            "reply": "Sorry, something went wrong while processing your request.",
            "cards": [],
            "sources": []
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )