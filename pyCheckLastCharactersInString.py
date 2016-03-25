#!/usr/bin/python

def pyCheckLastCharactersInString(string2study, characters2check):
	# check if string2study ends with characters2check
	# -characters2check: string
	numberCharacters2check = len(characters2check) # int
	stringLastCharacters = string2study[-numberCharacters2check:] # string
	if stringLastCharacters == characters2check:
		return 1
	else:
		return -1