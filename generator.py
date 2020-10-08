# I decided to use the secrets module which should be more secure and random then the math.randon function


# use Char code
import secrets
from enum import Enum

class charType(Enum):
    LOWER = 0
    UPPER = 1
    NUMBER = 2
    SPECIAL = 3


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuv'
specialCharacters = '!@#$%^&*()_+-={}[]\\|,.<>/?;:`~'
numbers = '1234567890'

reqNumChars = -1
reqNumUpperCase = -1
reqNumLowerCase = -1
reqNumNums = -1
reqNumSpecialChars = -1

# I originally was gonna use if else statements and Booleans to do error checking, might still need it
upperCaseCheck = False
lowerCaseCheck = False
specialCharactersCheck = False
numbersCheck = False


# Function to generate a random password from the given the specifications
def genAbstract(charSet):
    myStr = ''

    maxRange = len(charSet)

    rand = secrets.randbelow(maxRange)
    myStr = myStr + charSet[rand]

    return str(myStr)


def genLower():
    global reqNumLowerCase
    print('genLower')

    myStr = ''

    if reqNumLowerCase > 0:
        myStr = genAbstract(lowercase)
        reqNumLowerCase -= 1
    return myStr


def genUpper():
    global reqNumUpperCase
    print('genUpper')
    myStr = ''

    if reqNumUpperCase > 0:
        myStr = genAbstract(uppercase)
        reqNumUpperCase -= 1

    return myStr


def genNumber():
    global reqNumNums
    print('genNumber')

    myStr = ''

    if reqNumNums > 0:
        myStr = genAbstract(numbers)
        reqNumNums -= 1
    return myStr


def genSpecial():
    global reqNumSpecialChars
    print('genSpecial')

    myStr = ''

    if reqNumSpecialChars > 0:
        myStr = genAbstract(specialCharacters)
        reqNumSpecialChars -= 1
    return myStr


def passwordGenerator(password=''):

    global reqNumSpecialChars, reqNumNums, reqNumUpperCase, reqNumLowerCase

    # randomly pick a genType to generate
    genType = secrets.randbelow(4)

    if genType == 0:
        password += genLower()

    if genType == 1:
        password += genUpper()

    if genType == 2:
        password += genSpecial()

    if genType == 3:
        password += genNumber()

    if reqNumUpperCase <= 0 and reqNumLowerCase <= 0 and reqNumSpecialChars <= 0 and reqNumNums <= 0:

        print(password)
        return password

    print([reqNumUpperCase, reqNumLowerCase, reqNumSpecialChars, reqNumNums])
    passwordGenerator(password)


# While statement to collect user input with a try and except clause to handle incorrect inputs
def getConfig(callback):

    global reqNumSpecialChars, reqNumNums, reqNumUpperCase, reqNumLowerCase

    finished = False
    while not finished:
        if reqNumUpperCase < 0:
            try:
                reqNumUpperCase = int(input('How many upper case characters are required: \n'))
            except ValueError:
                print('Please enter a number!')
                continue

        if reqNumLowerCase < 0:
            try:
                reqNumLowerCase = int(input('How m any lower case characters are required: \n'))
            except ValueError:
                print('Please enter a number!')
                continue

        if reqNumNums < 0:
            try:
                reqNumNums = int(input('How many number characters are required: \n'))
            except ValueError:
                print('Please enter a number!')
                continue

        if reqNumSpecialChars < 0:
            try:
                reqNumSpecialChars = int(input('How many special characters are required: \n'))
            except ValueError:
                print('Please enter a number!')
                continue

        finished = True

    callback()


getConfig(passwordGenerator)