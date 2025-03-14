from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("⚠️ ERROR: OPENAI_API_KEY not set. Please export it before running.")


# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")  # Serves the frontend

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # GPT-4o Mini Model
            messages=[{"role": "user", "content": user_message}]
        )

        bot_response = response.choices[0].message.content.strip()
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

