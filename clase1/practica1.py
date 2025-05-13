import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print ("-------------------")
print ("---------------")  

USER_NAME=input("WHAT'S YOUR NAME? ")
print(f"HELLO {USER_NAME}!")
USER_LASTNAME=input("WHAT'S YOUR LAST NAME? ")
print(f"HELLO {USER_NAME} {USER_LASTNAME}!")

