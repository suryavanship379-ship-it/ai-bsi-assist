import sys
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from services.product_detector import detect_product
from services.response_service import generate_response

# Add AI/ML module to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
AI_ML_SRC = PROJECT_ROOT / "ai-ml" / "src"

sys.path.insert(0, str(AI_ML_SRC))

from rag_pipeline import get_ai_response


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

        # Try AI/ML RAG response
        try:
            ai_result = get_ai_response(message)

            if ai_result and ai_result.get("status") == "success":
                return jsonify({
                    "status": "success",
                    "reply": ai_result.get("reply", ""),
                    "cards": ai_result.get("cards", []),
                    "sources": ai_result.get("sources", [])
                })

        except Exception as ai_error:
            print("AI/ML error:", ai_error)
            print("Falling back to backend response service.")

        # Existing backend fallback
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