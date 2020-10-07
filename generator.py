import secrets
import sys


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuv'
specialCharacters = '!@#$%^&*()_+-={}[]\|,.<>/?;:`~'
numbers = '1234567890'

password = ''
upperCaseCheck = False
lowerCaseCheck = False
specialCharactersCheck = False
numbersCheck = False





print('This program is designed to generate a random passoword that with an option '
      'to have requirements')
reqNumOfChars = int(input('How many long must your password be: \n'))
reqNumUpperCase = int(input('How many upper case characters are required: \n'))
reqNumNums = int(input('How many numbers are required: \n'))
reqSpecialChars = input('Are specials characters required? Please type Yes or No \n')

random = secrets.randbelow(100)




counter = 0
while counter < reqNumOfChars:
    if reqSpecialChars == 'Yes' or 'Y' or 'y' or 'yes' or 'N' or 'n' or 'No' or 'no':
        password += specialCharacters[secrets.randbelow(10)]
        counter += 1
    else:
        password += uppercase[secrets.randbelow(26)]
        counter += 1
print(password)
