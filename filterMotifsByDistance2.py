"""
IN: distance file for all pair-wise distances between, distance (similarity) cutoff D

OUT: list of motifs with best AUCs ad 

"""

from sys import argv
import sys


def main():
	infile=argv[1]
	Dcutoff=float(argv[2])
	output=argv[3]

	motifnames={}
	motifstoremove={}
	lines=open(infile)
	distanceDict = {}
	print "parsing the file..."
	for line in lines:
		line = line.split()
		#print line
		#break
		motifA = line[0]
		motifB = line[1]
		if motifA not in motifnames:
			motifnames[motifA]=1
		if motifB not in motifnames:
			motifnames[motifB]=1
		if motifA in motifstoremove or motifB in motifstoremove:
			continue

		d = float(line[2])
	
		if d <Dcutoff and line[0]!=line[1]: #condition to remove a motif, deciding which to remove
			#print line
			pvalueA=float(motifA.split('_')[-1])
			pvalueB=float(motifB.split('_')[-1])
			if pvalueA<=pvalueB: 
				#remove B
				motifstoremove[motifB]=1
			else:
				motifstoremove[motifA]=1



	#Based on the distanceDict, remove certain motifs based on their p-value
	motifstokeep=[]
	for motif in motifnames:
		if motif not in motifstoremove:
			motifstokeep+=[motif]
	print len(motifnames),len(motifstoremove),len(motifnames)-len(motifstoremove)
	
	outfile=open(output,'w')
	for motif in motifstokeep:
		outfile.write(motif+'\n')
	outfile.close()

	return 


if __name__=="__main__":
	main()