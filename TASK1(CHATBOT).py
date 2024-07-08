print("------------------------------------------------CHATBOT-------------------------------------------------")
print("----------------------------------------------ASK A QUERY-----------------------------------------------")
print("NOTE:It is case sensitive CHATBOT. So, Type your Queries correctly.")
print("->hi")
print("->hello")
print("->what is your name?")
print("->what is your age?")
print("->what did you eat?")
print("->does AI replaces human in future?")
print("->Is AI is harmful to the Human resource?")
print("->what is CODSOFT?")
print("->Thankyou")
print("->bye")

trained_command = {
    "hi": "Hi there! I'm here to assist you?",
    "hello": "Hello! Let me help you, what's your Query?",
    "what is your name?": "My Owner named me as a Ritzbot!!",
    "what is your age?": "I am a machine, I dont have age like humans.",
    "what did you eat?": "LOL, I eat your device power and Data.",
    "does AI replaces human in future?": "Definately not, for Ex: mathematician is neccesary for critical tasks, calculator is not enough",
    "Is AI is harmful to the Human resource?": "It Depends, If not use properly it will cause loss",
    "what is CODSOFT?": "It is IT consultancy and services, where they are passionate about technology and software to change the world",

}


def get_response(user_query):
    for pattern, response in trained_command.items():
        if pattern in user_query:
            return response
    return "I'm sorry, this is untrained Query.Can you please rephrase your sentence?"


print("Chatbot: Hi! I'm a Well-trained chatbot,I'm here to assist you!")
while True:
    user_query = input("Me: ")
    if user_query == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    if user_query == "Thankyou":
        print("Chatbot: welcome sir/madam, any other query?")
    else:
        response = get_response(user_query)
        print("Chatbot:", response)
