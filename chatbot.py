pip install nltk
import nltk
from nltk.stem import PorterStemmer
from nltk.chat.util import Chat
nltk.download('punkt')
nltk.download('wordnet')
pairs = [
    ["Happy", "Birthday"],
    ["- IQRA <3", "May ALLAH grant you with lots of love, health, happiness, adventures, luck. beauty and excietment in your life."],
    ["I Love You."],
]
def chatbot():
    chat = Chat(pairs, reflection="you")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        print(chat.respond(- I LOVE YOU <3))

if __name__ == "__main__":
    chatbot()
