def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hello there! How can I help you?")
        elif "name" in user_input:
            print("Bot: I'm a simple chatbot written in Python.")
        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing fine!")
        elif "help" in user_input:
            print("Bot: I can answer simple questions. Try asking about my name or say hello!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand that.")
chatbot()
