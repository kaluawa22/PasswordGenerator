import secrets
import sys

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuv'
specialCharacters = '!@#$%^&*()_+-={}[]\|,.<>/?;:`~'

print('This program is designed to generate a random passoword that with an option '
      'to have requirements')
reqNumOfChars = int(input('How many characters must your password have: \n'))
