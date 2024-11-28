import random

responses = {
    'hello': 'Hi there!',
    'how are you': 'I am good, how about you?',
    'bye': 'Goodbye! Have a nice day!',
    'joke': ['Why don’t skeletons fight each other? They don’t have the guts.', 
             'I told my wife she was drawing her eyebrows too high. She looked surprised.']
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == 'joke':
        return random.choice(responses[user_input])
    return responses.get(user_input, "Sorry, I don't understand.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
