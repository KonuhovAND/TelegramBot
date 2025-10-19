import os


def ask_your_token():
    if not os.path.exists('./keys/_token.py'):
        token= input("Enter your telegram bot token: ")
        with open('./keys/_token.py','w') as file:
            file.write(f"_token= '{token}'\n") 
