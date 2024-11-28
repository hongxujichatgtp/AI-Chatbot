from flask import Flask, jsonify, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the AI Chatbot!'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
