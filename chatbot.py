import nltk
from nltk.chat.util import Chat, reflections

# Define an expanded list of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you!']),
    (r'quit', ['Bye! Take care!']),
    (r'what time is it?', ['I am not sure about the time, but you can check it on your device.']),
    (r'how is the weather', ['I don\'t have access to weather information right now.']),
    (r'where are you from?', ['I am a chatbot and don\'t have a physical location.']),
    (r'(.*) your favorite color?', ['I don\'t have personal preferences, but I like all colors!']),
    (r'(.*) (sports|game)', ['I like many sports. Do you have a favorite?']),
    (r'(.*) (food|dish)', ['I don\'t eat, but I hear pizza is very popular!']),
    (r'(.*) help', ['How can I assist you?'])
]

# Create a chatbot with the defined patterns and responses
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
