from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your OpenRouter API Key
OPENROUTER_API_KEY = "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"

def get_openrouter_response(user_message):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    try:
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    bot_response = get_openrouter_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
