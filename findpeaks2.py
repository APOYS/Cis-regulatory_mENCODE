import os 
from sys import argv

dir=argv[1]
print dir
fs = os.listdir(dir)
Input = ""
files=[]
for f in fs:
	if "bed" in f:
		files+=[f]
print files
for i in range(len(files)):
	if "INPUT" in files[i].upper():
		Input = files.pop(i)
		#print Input
		break

for mark in files:
	print "Finding Peaks in "+ mark
	Findpeak1= "findPeaks " + mark + " -style histone -fragLength 290 -i " + Input + " -inputFragLength 290 -tbp 1 -inputtbp 1 > " + mark.split(".bed")[0]+".1.peaks"
    	Findpeak2= "findPeaks " + mark +" -region -size 1000 -minDist 2500 -fragLength 290 -i "+ Input + " -inputFragLength 290 -tbp 1 -inputtbp 1 > " + mark.split(".bed")[0]+".2.peaks"
	print Findpeak1
	#os.system(Findpeak1)
	print Findpeak2
	#os.system(Findpeak2)
