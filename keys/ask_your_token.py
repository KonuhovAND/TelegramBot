import os

token= input("Enter your telegram bot token: ")
    
with open('./keys/_token.py','w') as file:
    file.write(f"_token= '{token}'\n") 
