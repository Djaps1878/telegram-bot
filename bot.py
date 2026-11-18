import requests

BOT_TOKEN = "OVDJE_STAVI_NOVI_TOKEN"
CHAT_ID = "-1004314206178"

message = "Hello! GitHub bot is working!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print(response.json())
