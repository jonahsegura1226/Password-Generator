import random
import string
print("Welcome to Password Generator!") # Just a Hi
thelength = int(input("Enter the length of the password: "))


def generatepassword(thelength): 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(thelength))
    return password

print("Password generator is ready!")
print("Generated Password:", generatepassword(thelength))
