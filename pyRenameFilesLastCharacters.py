#!/usr/bin/python

from os.path import join
from pyCheckLastCharactersInString import pyCheckLastCharactersInString
from pyRenameFile import pyRenameFile
from pyRenameLastCharactersOfString import pyRenameLastCharactersOfString

def pyRenameFilesLastCharacters(filesPath, filesName, whatChange):
	# changes indicated last part of files name
	# inputs
	# -filesPath: str
	# -filesName: list of one or more strings
	# -whatchange: list of two strings. String one: original characters to change. String two: new characters
	oldCharacters = whatChange[0]	
	newCharacters = whatChange[1]
	for oldFileName in filesName:
		if pyCheckLastCharactersInString(oldFileName,oldCharacters) == 1:
			newFileName = pyRenameLastCharactersOfString(oldFileName, oldCharacters, newCharacters)
			filePathAndName = join(filesPath,oldFileName)
			pyRenameFile(filesPath, oldFileName, newFileName)
		else:
			print 'Warning. No modified: '+str(oldFileName)
	return 1