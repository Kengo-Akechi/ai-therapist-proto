import requests
import json

def get_bot_response(user_input):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are a compassionate AI therapist. Always respond with empathy and understanding."},
            {"role": "user", "content": user_input}
        ]
    }

    # Make streaming POST request
    response = requests.post(url, headers=headers, json=payload, stream=True)

    # Join all streamed content
    full_reply = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            content = data.get("message", {}).get("content", "")
            full_reply += content

    return full_reply.strip()
