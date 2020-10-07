# I decided to use the secrets module which should be more secure and random then the math.randon function

import secrets
import sys


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuv'
specialCharacters = '!@#$%^&*()_+-={}[]\|,.<>/?;:`~'
numbers = '1234567890'
password = ''
# I originally was gonna use if else statements and Booleans to do error checking, might still need it
upperCaseCheck = False
lowerCaseCheck = False
specialCharactersCheck = False
numbersCheck = False

notFinished = True

# Functiot to genrate the random password given the specifications

def passwordGenerator(password, numChars, numUppercase, numLowercase, reqSpecialChar, numNums):
    counter = 0
    while counter < numChars:
        if reqSpecialChar == 'Yes' or 'Y' or 'y' or 'yes' or 'N' or 'n' or 'No' or 'no':
            password += specialCharacters[secrets.randbelow(len(specialCharacters))]
            counter += 1
    print(password)



print('This program is designed to generate a random passoword that with an option '
      'to have requirements')





# While statement to collect user input with a try and except clause to handle incorrect inputs
while notFinished:
    try:
        reqNumOfChars = int(input('How many long must your password be: \n'))
    except ValueError:
        print('Please enter a number!')
        reqNumOfChars = int(input('How many long must your password be: \n'))
    try:
        reqNumUpperCase = int(input('How many upper case characters are required: \n'))
    except ValueError:
        print('Please enter a number!')
        reqNumUpperCase = int(input('How many upper case characters are required: \n'))
    try:
        reqNumLowerCase = int(input('How m any lower case characters are required: \n'))
    except ValueError:
        print('Please enter a number!')
        reqNumLowerCase = int(input('How m any lower case characters are required: \n'))
    try:
        reqNumNums = int(input('How many number characters are required: \n'))
    except ValueError:
        print('Please enter a number!')
        reqNumNums = int(input('How many number characters are required: \n'))
    try:
        reqSpecialChars = input('Are special characters required: \n')
    except ValueError:
        print('Please enter Yes or No!')
        reqSpecialChars = input('Are special characters required: \n')
    notFinished = False


# reqNumOfChars = int(input('How many long must your password be: \n'))
# reqNumUpperCase = int(input('How many upper case characters are required: \n'))
# reqNumLowerCase = int(input('How many lower case characters are required: \n'))
# reqNumNums = int(input('How many numbers are required: \n'))
# reqSpecialChars = input('Are specials characters required? Please type Yes or No \n')

passwordGenerator(password, reqNumOfChars, reqNumUpperCase, reqNumLowerCase, reqSpecialChars, reqNumNums)

random = secrets.randbelow(100)



#
# counter = 0
# while counter < reqNumOfChars:
#     if reqSpecialChars == 'Yes' or 'Y' or 'y' or 'yes' or 'N' or 'n' or 'No' or 'no':
#         password += specialCharacters[secrets.randbelow(10)]
#         counter += 1
#     else:
#         password += uppercase[secrets.randbelow(26)]
#         counter += 1
# print(password)

# %%#&!*