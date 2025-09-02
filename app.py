# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from model.chatbot import get_bot_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask is running. Chat endpoint is at /chat"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')
    
    if not user_msg:
        return jsonify({'response': "Please enter a message."}), 400

    bot_reply = get_bot_response(user_msg)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
