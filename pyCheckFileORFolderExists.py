#!/usr/bin/python

import os
from os.path import join

def pyCheckFileORFolderExists(path, name, folderORfile):
	# variables
	# input:
	# - path: string. path of the folder or file to study
	# - name: string. name of the folder or file to study. None if path has all the path (path+name of what study)
	# - folderORfile: string ('folder' or 'file'). Indicates whate to check if a folder or a file
	# output:
	# - 1: exists
	# - -1: doesn't exist
	if name != None:
		pathAndName = join(path,name)
	if name == None:
		pathAndName = path
	if folderORfile == 'folder':
		exists = os.path.isdir(pathAndName) # True or False
	elif folderORfile == 'file':
		exists = os.path.isfile(pathAndName) # True or False
	if exists == True: 
		return 1
	elif exists == False:
		return -1
