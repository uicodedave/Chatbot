import random

data = {
    "hi" : ["Hey!", "Hello!", "Hi there"],
    "how are you?" : ["I'm good!", "Doing great, thanks!"],
    "bye" : ["See you soon!", "Goodbye!", "Take care!"],
    "what is your name" : ["I'm DavidBot!", "They call me DavidBot"]
}

#Welcome message
# \n means move to the next line
print("Welcome to Davidbot! Type something to chat. Type 'exit' to quit. \n") 

#chat loop
# while is a type of loop and it keeps running until a condition is made
# break means to stop the loop, if you dont add break it keeps running
# strip removes every space

while True:
    user_input = input("You: ").lower().strip() #take input, make it lowercase
    if user_input == "exit":
        print("DavidBot: Goodbye")
        break
    elif user_input in data:
            print("DavidBot:", random.choice(data[user_input]))
    else:
        print("DavidBot: I don’t understand that yet.")