import os
from sys import argv

beddir=argv[1]



def isBroadorNarrow(s):
	narrow=["H3K4me1","H3K4me2","H3K4me3","H3K27ac","H3K9ac"]
	broad=["H3K9me3","H3K27me3","H3K36me3"]
	for i in narrow:
		if i in s:
			return "narrow"
	for j in broad:
		if j in s:
			return "broad"
	return

bedfiles=[]
for file in os.listdir(beddir):
	if '.bed' in file:
		bedfiles+=[file]
print "Number of files",len(bedfiles)
#narrowPeaks
for f in bedfiles:
	peaktype=isBroadorNarrow(f)
	#print peaktype
	if peaktype=="narrow":
		os.system("mergeBed -d 1000 -i "+ beddir+'/'+f+" > "+f.replace(".bed",".narrowPeaks.bed"))
	elif peaktype=="broad":
		os.system("mergeBed -d 2500 -i "+ beddir+'/'+f+" > "+f.replace(".bed",".broadPeaks.bed"))
	else:
		print "ERROR, no type detected"


