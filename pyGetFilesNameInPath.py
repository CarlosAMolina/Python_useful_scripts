#!/usr/bin/python

from os.path import isfile, join

def pyGetFilesNameInPath(archivesPath,archivesName): # get only files
	# archivesName: all archives in the path (folders, etc.)
	filesName=[] # save archives that are files (not folders for example)
	for archiveName in archivesName:
		archivePathAndName = join(archivesPath,archiveName)
		if isfile(archivePathAndName)==True:
			filesName.append(archiveName)
	return filesName