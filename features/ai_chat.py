import requests
from voice.tts import say
from config.settings import OPENROUTER_API_KEY

def chat_with_ai(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Jarvis AI Assistant"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"].strip()
            say(reply)
            print("AI:", reply)
            return reply
        else:
            say("AI response error")
    except Exception as e:
        print("Error:", e)
        say("Connection failed")
