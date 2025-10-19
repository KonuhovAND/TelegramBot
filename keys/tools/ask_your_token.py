import os


def ask_your_token():
    if not os.path.exists('./keys/token.py'):
        token= input("Enter your telegram bot token: ")
        with open('./keys/token.py','w') as file:
            file.write(f"token= '{token}'\n") 
