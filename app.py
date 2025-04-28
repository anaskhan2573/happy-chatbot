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
    data = response.json()

    if 'choices' in data:
        reply = data['choices'][0]['message']['content']
    else:
        print("API error:", data)
        reply = "Sorry, there was an error: " + str(data.get('error', 'Unknown error'))


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
