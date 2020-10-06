import secrets
import sys


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuv'
specialCharacters = '!@#$%^&*()_+-={}[]\|,.<>/?;:`~'
password = ''

print('This program is designed to generate a random passoword that with an option '
      'to have requirements')
reqNumOfChars = int(input('How many characters must your password have: \n'))
reqSpecialChars = input('Are specials characters required? Please type Yes or No \n')

random = secrets.randbelow(100)

counter = 0

while counter < reqNumOfChars:
    password += uppercase[secrets.randbelow(26)]
    counter += 1
print(password)