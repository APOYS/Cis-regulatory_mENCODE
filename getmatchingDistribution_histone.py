import os
from sys import argv

fileA = argv[1]
fileBdir = argv[2] #look for files in this dir, then compare all of them against the fileA
mark = argv[3]


result = {}
for i in range(1,11):
	result[str(i)] = []

markfiles = os.listdir(fileBdir) #these files jave been binned 10 windows
for file in markfiles:
	if mark in file:
		print file
		fileB = fileBdir+'/'+file
		command = "intersectBed -a "+fileA+" -b "+fileB+" -wb> X.tmp.test"
		#print command
		os.system(command)
		#intersectbed 
		os.system("cut -f10 X.tmptest |sort| uniq -c|sort -k2n >X.tmp.distro")
		lines = open("X.tmp.ditro").read().split('\n')
		for l in lines:
			tmp = l.strip().split()
			result[tmp[1]] = int(tmp[0])
print result

