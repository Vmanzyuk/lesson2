ask_library={"Whats up ?": "Good", "What do you do ?": "Programming"}

def ask_user():
    while True:
        try:
            user_say=input('Pls enter your question:')
            if ask_library.get(user_say):
            
                print (ask_library[user_say])
                break
        except (KeyboardInterrupt):
            print('Good luck')
    return

ask_user()

