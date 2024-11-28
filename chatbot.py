import random

responses = {
    'hello': 'Hi there!',
    'how are you': 'I am good, how about you?',
    'bye': 'Goodbye! Have a nice day!'
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
