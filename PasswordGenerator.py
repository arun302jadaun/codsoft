import random
import string

def password(min_length,numbers=True,specialCharacters=True):
    letters = string.ascii_letters
    digits =string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special

    pw = ""
    criteria = False
    has_numbers = False
    has_special =  False

    while not criteria or len(pw)<min_length :
        new_char = random.choice(characters)

        pw += new_char

        if new_char in digits :
            has_numbers = True
        elif new_char in special:
            has_special = True

        criteria = True
        if numbers:
            criteria = has_numbers
        if specialCharacters:
            criteria = criteria and has_special

    return pw      



print('HELLO USER :>') 
print('I hope you doing great ! ')
print('Okay so lets focus on password generation process....')


min_Length = int(input("So, tell me what should be the length of your password: "))
has_numbers = input("Do you want numbers in your desired password (T/F) ? ").upper()=="T"
has_special = input("Do you want special characters in your desired password (T/F) ? ").upper()=="T"
pw = password(min_Length, has_numbers, has_special )
print("okay, user so according to all your entries")
print("Your generated password is : ",pw)
          