# I decided to use the secrets module which should be more secure and random then the math.randon function



# use Char code

import secrets
import sys

uppercase 			= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase 			= 'abcdefghijklmnopqrstuv'
specialCharacters 	        = '!@#$%^&*()_+-={}[]\|,.<>/?;:`~'
numbers 			= '1234567890'
password 			= ''

# I originally was gonna use if else statements and Booleans to do error checking, might still need it
upperCaseCheck 			= False
lowerCaseCheck 			= False
specialCharactersCheck 	        = False
numbersCheck 			= False
finished 			= False

# Function to generate a random password from the given the specifications
def genAbstract(count, charSet):
	done 	= false 
	str 	= ''
	
	maxRange = len(charSet)
	
	
	
	while not done:
		
		rand 	= secrets.randbelow(maxRange)
		str 	= str + charset[rand]
		
		done 	= len(str) == count

	return str

def genLower(count):
	str = genAbstract(count, lowercase)
	return str
	
def genUpper(count):
	str = genAbstract(count, upper)
	return str
	
def genNums(count):
	str = genAbstract(count, numbers)
	return str
	
def genSpecial(count):
	str = genAbstract(count, specialCharacters)
	return str


def passwordGenerator(password, numChars, numUppercase, numLowercase, reqSpecialChar, numNums):
    counter = 0
	
	
    reqSpecialChar = reqSpecialChar.lower()
	
    if reqSpecialChar in ['y', 'yes']:
        password += specialCharacters[secrets.randbelow(len(specialCharacters))]
	counter += 1	
	
    while counter < numChars:
        if reqSpecialChar == 'Yes' or reqSpecialChar == 'Y' or reqSpecialChar == 'y' or reqSpecialChar == 'yes' or reqSpecialChar == 'N' or reqSpecialChar == 'n' or reqSpecialChar == 'No' or reqSpecialChar == 'no':

    print(password)


print('This program is designed to generate a random passoword that with an option '
      'to have requirements')



# While statement to collect user input with a try and except clause to handle incorrect inputs
reqNumChars 		= False
reqNumUpperCase 	= False
reqNumLowerCase 	= False
reqNumNums 			= False
reqSpecialChars 	= False

while not finished:

	#check if reqNumChars is set 
	
	if reqNumChars == false:
		try:
			reqNumOfChars = int(input('How many long must your password be: \n'))
		except ValueError:
			print('Please enter a number!')
			continue
		
	if reqNumUpperCase == false:		
		try:
			reqNumUpperCase = int(input('How many upper case characters are required: \n'))
		except ValueError:
			print('Please enter a number!')
			continue
			
	if reqNumLowerCase == false:		
		try:
			reqNumLowerCase = int(input('How m any lower case characters are required: \n'))
		except ValueError:
			print('Please enter a number!')
			continue
			
	if reqNumNums == false:		
		try:
			reqNumNums = int(input('How many number characters are required: \n'))
		except ValueError:
			print('Please enter a number!')
			continue
			
	if reqSpecialChars == false:
		try:
			reqSpecialChars = input('Are special characters required: \n')
		except ValueError:
			print('Please enter Yes or No!')
			continue
		
    finished = True


passwordGenerator(password, reqNumOfChars, reqNumUpperCase, reqNumLowerCase, reqSpecialChars, reqNumNums)



