#!/usr/bin/python


def pyDeleteFirsLastCharacter(string2change):

	# quit fist and last character of a string. Example: 'home/user' -> home/user
	# variables:
	# -input: string
	# -output: string
	
	if len (string2change) > 2:
		newString = string2change[1:] # delete first character
		newString = newString[:-1] # delete last character
		return newString
	else:
		print 'ERROR pyDeleteFirsLastCharacter. String must have more than 2 characters'
		return -1
