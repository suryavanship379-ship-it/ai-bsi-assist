/**
 * BIS Mitra - Frontend API Service
 * Connects the React frontend with the Flask backend.
 */

const API_BASE_URL = "http://127.0.0.1:5000";

/**
 * Send a message to BIS Mitra backend.
 *
 * @param {string} message
 * @param {Array} conversationHistory
 * @returns {Promise<Object>}
 */
export async function sendMessage(message, conversationHistory = []) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        conversationHistory,
      }),
    });

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    const data = await response.json();

    return {
      text: data.reply || "Sorry, I could not generate a response.",
      cards: data.cards || [],
      sources: data.sources || [],
    };
  } catch (error) {
    console.error("BIS Mitra API Error:", error);

    return {
      text:
        "Sorry, I couldn't connect to the BIS Mitra backend. Please make sure the Flask server is running.",
      cards: [],
      sources: [],
    };
  }
}