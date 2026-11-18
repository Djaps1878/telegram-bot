
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "-1004314206178"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    commits = data.get("commits", [])

    print("NUMBER OF COMMITS:", len(commits))

    for commit in commits:
        author = commit.get("author", {}).get("name", "Unknown")
        message = commit.get("message", "No message")
        url = commit.get("url", "")

        text = (
            "🚀 NEW COMMIT PUSHED TO GITHUB!\n\n"
            f"👤 Author: {author}\n"
            f"📝 Commit Message: {message}\n"
            f"🔗 View Commit: {url}"
        )

        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": text
            },
            timeout=10
        )

        print("TELEGRAM STATUS:", response.status_code)
        print("TELEGRAM RESPONSE:", response.text)

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
