#!/usr/bin/python

import re
from pyDeleteCharacter import pyDeleteCharacter

def pyGetImageNameFromPathAndName(filePathAndName):

	# input. filePathAndName: str contains path+fileName. Example /user/desktop/car.jpg
	# output: two strings. filaPath, fileName

	filePathAndNameList = re.compile('/').split(filePathAndName)
	fileName = filePathAndNameList[-1]
	filePath = pyDeleteCharacter(filePathAndName, fileName)[0] # pyDeleteCharacter return a list
	return filePath, fileName