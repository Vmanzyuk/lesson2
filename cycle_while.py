ask_library={"Whats up ?": "Good", "What do you do ?": "Programming"}

def ask_user():
    while True:
        user_say=input('Pls enter your question:')
        if ask_library.get(user_say):
            
            print (ask_library[user_say])
            break
    return

ask_user()

