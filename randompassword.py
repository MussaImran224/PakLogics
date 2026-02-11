import string
import random

print("Welcome to Random Password Generator")
print("Enter Password Length")
length = int(input())
print('''Choose characters for password from these : \n 1. Digits\n2. Letters\n3. Special characters\n4. Exit''')
character_List = ""
while(True):
    print("Pick a Number")
    choice = int(input())
    if(choice == 1):
        character_List =character_List + string.ascii_letters
    elif(choice == 2):
        character_List =character_List + string.digits
    elif(choice == 3):
        character_List =character_List + string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password= []

for i in range(length):
    randomchar = random.choice(character_List)
    password.append(randomchar)
print("The random password is: ", password)