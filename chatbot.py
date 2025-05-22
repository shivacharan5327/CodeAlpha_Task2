def chatbot():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if "hello" in user_input:
            print("Bot: Hello there!")
        elif "how are you" in user_input:
            print("Bot: I'm fine, thanks!")
        elif "bye" in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that.")

if __name__ == "__main__":
    chatbot()
