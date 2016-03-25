#!/usr/bin/python

from os.path import join
from pyCommandLine import pyCommandLine

def pyRenameFile(filePath, fileNameOld, fileNameNew):
	# variables
	# input: str (can be only te fileName or filePath+'/'+fileName)
	# output: str
	fileNameAndPathOld = join(filePath,fileNameOld)
	fileNameAndPathNew = join(filePath,fileNameNew) # use all the path to avoid the file changes its directory
	try:
		command = ['mv',fileNameAndPathOld,fileNameAndPathNew]
		return pyCommandLine(command)
	except:
		return -1