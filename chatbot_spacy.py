import spacy
from spacy.matcher import Matcher

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define patterns and responses
patterns = {
    'greeting': [{'LOWER': 'hi'}, {'LOWER': 'hello'}, {'LOWER': 'hey'}],
    'how_are_you': [{'LOWER': 'how'}, {'LOWER': 'are'}, {'LOWER': 'you'}],
    'name': [{'LOWER': 'name'}],
    'quit': [{'LOWER': 'quit'}],
    'weather': [{'LOWER': 'weather'}],
    'time': [{'LOWER': 'time'}],
    'sports': [{'LOWER': 'sports'}, {'LOWER': 'game'}],
    'food': [{'LOWER': 'food'}, {'LOWER': 'dish'}],
    'joke': [{'LOWER': 'joke'}, {'LOWER': 'funny'}],
    'thanks': [{'LOWER': 'thank'}, {'LOWER': 'thanks'}],
    'favorite_color': [{'LOWER': 'favorite'}, {'LOWER': 'color'}],
    'help': [{'LOWER': 'help'}]
}

# Initialize spaCy Matcher
matcher = Matcher(nlp.vocab)
for key, pattern in patterns.items():
    matcher.add(key, [pattern])

def get_response(text):
    doc = nlp(text)
    matches = matcher(doc)
    responses = {
        'greeting': 'Hello! How can I assist you today?',
        'how_are_you': 'I am doing great, thank you! How about you?',
        'name': 'I am your friendly chatbot, here to help you!',
        'quit': 'Goodbye! Have a wonderful day!',
        'weather': 'I can’t check the weather right now, but you can check your local weather app.',
        'time': 'I don’t have access to the current time, but you can check your device for that.',
        'sports': 'I like many sports! Do you have a favorite sport or team?',
        'food': 'I don’t eat, but I’ve heard sushi is quite popular!',
        'joke': 'Why did the scarecrow win an award? Because he was outstanding in his field!',
        'thanks': 'You’re welcome! If you need anything else, just ask.',
        'favorite_color': 'I don’t have a favorite color, but I hear blue is quite calming.',
        'help': 'I am here to help you. What do you need assistance with?'
    }
    for match_id, start, end in matches:
        match_id_str = nlp.vocab.strings[match_id]
        return responses.get(match_id_str, 'Sorry, I don\'t understand.')
    return 'Sorry, I don\'t understand.'

def chat():
    print("Hi! I'm a spaCy-powered chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
