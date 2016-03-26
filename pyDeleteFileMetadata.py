#!/usr/bin/python

from pyCommandLine import pyCommandLine
from os.path import join

# Note: if metadata of the image had been removed before, now the file won't be modified

def pyDeleteFileMetadata(filePath, fileName=None):
	# variables
	# input. filePath: str. fileName: str or None if filePath contains the path and the fileName
	# output: int
	try:
		if fileName == None: # the user puts the filename in filePath
			fileNameAndPath = filePath
		else:
			fileNameAndPath = join(filePath,fileName)
		command = ['exiftool', '-all=',str(fileNameAndPath)]
		result = pyCommandLine(command)
		if 'imagefilesunchanged' in result: # if the metadatas were removed previously, the file won't be modified
			print 'WARNING: file ' + str(fileName) + " doesn't change (metadata must be already deleted)"
			return -1
		else:
			return 1
	except:
		print 'ERROR delete metadata. File: ' + str(fileName)
		return -1