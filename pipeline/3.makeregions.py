import os 
from sys import argv

beddir=argv[1]
uniqueomefile=argv[2]

bedfiles=[]
for f in os.listdir(beddir):
	if "Peaks.bed" in f:
		bedfiles+=[f]

for f in bedfiles:
	command="subtractBed -a "+uniqueomefile +"-b "+beddir+'/'+f +" -A  > "+f.replace('.bed','.rest.bed')
	print command
	#os.system(command)

