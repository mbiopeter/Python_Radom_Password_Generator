# Ask the user if thet want to generate the password or not
# If yes ask for the password llength
# Generate the password
# Print the password
# If the innitial response is no exit the program

import string
import random
character = list(string.ascii_letters + string.digits + "@!#$%*^&*()")

def generate_password():
    password_llength = int(input("Enter your password Length:"))

    random.shuffle(character)
    password = []

    for x in range(password_llength):
        password.append(random.choice(character))
    random.shuffle(password)

    password ="".join(password)
    print(password)

option = input("Do you want to generate the password? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("programe edded")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()