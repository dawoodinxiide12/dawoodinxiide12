pip install nltk
import nltk
from nltk.stem import PorterStemmer
from nltk.chat.util import Chat
nltk.download('punkt')
nltk.download('wordnet')
pairs = [
    ["hello", "Hi there!"],
    ["how are you?", "I'm doing well, thanks for asking."],
    ["what is your name?", "My name is Chatbot."],
]
def chatbot():
    chat = Chat(pairs, reflection="you")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        print(chat.respond(user_input))

if __name__ == "__main__":
    chatbot()
