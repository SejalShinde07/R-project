print("Hello! I'm Rulebot")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm learning more skills , but I'm doing great! ")
    elif "your name" in user_input:
        print("Bot: I'm RuleBot, your friendly chatbot.")
    elif "help" in user_input:
        print("Bot: I can respond to greetings, tell you my name, and chat a bit. Try saying 'hello' or ask 'how are you'.")
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day! ")
        break
    else:
        print("Bot: Sorry, I didn't understand that. Try saying 'help'.")

