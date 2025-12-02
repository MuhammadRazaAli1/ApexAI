def chatbot_reply(user_input):
    user_input = user_input.lower()  # convert input to lowercase for easy matching

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm a virtual assistant, I don't have physical appearance. But I'm doing great!\nHow can I help you tpday?"
    elif "oh great" in user_input:
        return "Thanks! What type of help you want from me?"
    elif "tell me what's your name" in user_input:
        return "I'm AI Chatbot, your friendly assistant."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're most welcome!"
    else:
        return "Sorry, I didn’t understand that. Could you please rephrase?"

# Main chat loop
print("Welcome to Apex Chatbot!\nYour Personal Assistant. 🤖 How can I help you today?")

while True:
    user_input = input("You: ")

    # Check if user wants to exit
    if "bye" in user_input.lower():
        print("Bot: Goodbye! See you again soon!")
        break

    # Get bot reply and print it
    reply = chatbot_reply(user_input)
    print("Bot:", reply)
