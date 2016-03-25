#!/usr/bin/python

from pyDeleteLastWhiteSpace import pyDeleteLastWhiteSpace
from pyDeleteFirsLastCharacter import pyDeleteFirsLastCharacter

def pyDeleteCommasPath(string2change):

	# if the path has simple commas at the beggining and in the end, quit them. If not, return the same string
	# example: 'Example: 'home/user' -> home/user'
	# variables:
	# -input: string
	# -output: string
	string2change = pyDeleteLastWhiteSpace(string2change) # because when a folder is drop to terminal, the route ends with a space
	if string2change[0] == "'" and string2change[-1] == "'":
		newString = pyDeleteFirsLastCharacter(string2change)
		return newString
	else:
		return string2change