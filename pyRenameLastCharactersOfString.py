#!/usr/bin/python

def pyRenameLastCharactersOfString(oldString, oldCharacters, newCharacters):
	# change last indicated characters of a string with the new ones
	# variables
	# input:
	# -oldString: string to change last characters
	# -oldCharacters: last characters of the name tat will be changed
	# -newCharacters: what to put instead oldCharacters
	# output:
	# -newString: renamed string
	newString = oldString[:-len(oldCharacters)]+newCharacters
	return newString