#!/usr/bin/python

from os import listdir

def pyGetArchivesNameInPath(archivesPath):  # all archives, example: folders, files, etc
	# output: list of strings (no elements -> []). Or -1 if an error occurs
	try:
		archivesName = listdir(archivesPath) # if only one elemente it return a list on one string
	except:
		archivesName = -1
	return archivesName
