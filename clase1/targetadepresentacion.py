import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print ("-------------------")
print ("---------------")

job=input("WHAT'S YOUR job? ")
lastname=input("WHAT'S YOUR LAST NAME? ")
name=input("WHAT'S YOUR NAME? ")
age=input("WHAT'S YOUR AGE? ")
Phone=input("WHAT'S YOUR PHONE? ")
email=input("WHAT'S YOUR EMAIL? ")
clear_screen()
print ("-------------------")
print ("---------------")
print( job)
print( f"{lastname} {name}, {age} years old")
print( Phone)   
print( email)
print ("-------------------")
print ("---------------")