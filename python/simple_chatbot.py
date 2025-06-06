"""Simple rule-based chatbot for beginners."""

def get_response(text: str) -> str:
    """Return a canned response based on user input."""
    text = text.lower().strip()
    if 'hello' in text or 'hi' in text:
        return 'Hello! How can I help you today?'
    if 'bye' in text or 'exit' in text:
        return 'Goodbye!'
    if 'help' in text:
        return 'I can respond to simple greetings and farewells.'
    return "I'm not sure how to respond to that."

def main():
    print("Type 'exit' to end the conversation.")
    while True:
        user = input('You: ')
        if user.lower().strip() == 'exit':
            print('Bot: Goodbye!')
            break
        print('Bot:', get_response(user))

if __name__ == '__main__':
    main()
