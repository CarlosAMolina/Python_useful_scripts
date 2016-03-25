#!/usr/bin/python

def pyDeleteLastWhiteSpace(string2change):

	# if the string ends with a space (occurs when a folder is drop to terminal and the path appears), quit it
	# variables:
	# -input: string
	# -output: string
	if string2change[-1] == " ": # if string ends with a space
		newString = string2change[:-1] # quit space at the end of the string
		return newString
	else:
		return string2change