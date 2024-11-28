import random

responses = {
    'hello': 'Hi there!',
    'how are you': 'I am good, how about you?',
    'bye': 'Goodbye! Have a nice day!',
    'help': 'I can help you with basic questions. Just ask!'
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand.")
