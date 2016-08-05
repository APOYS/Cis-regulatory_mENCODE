"""
IN: distance file for all pair-wise distances between, distance (similarity) cutoff D

OUT: list of motifs with best AUCs ad 

"""

from sys import argv
import sys


def main():
	infile="Chosen.Allmotifs.0.2_0.3.renamed.filtered.389.dist.sorted.txt"
	Dcutoff=0.1

	motifnames={}
	
	lines=open(infile).readlines()
	distanceDict = {}
	print "parsing the file..."
	for line in lines:
		line = line.split()
		#print line
		motifA = line[0]
		motifB = line[1]
		if motifA not in motifnames:
			motifnames[motifA]=1
		if motifB not in motifnames:
			motifnames[motifB]=1


		d = float(line[2])
		
		if d <Dcutoff and line[0]!=line[1]:
			#print line
			try:
				distanceDict[motifA][motifB]=d
			except KeyError:
				distanceDict[motifA]={}
				distanceDict[motifA][motifB]=d



	#Based on the distanceDict, remove certain motifs based on their p-value
	#print motifnames
	print len(motifnames)
	motifstoremove={}
	for motifA in distanceDict:
		#print motifA
		removeA=False
		pvalueA=float(motifA.split('_')[-1])
		for motifB in distanceDict[motifA]:
			pvalueB=float(motifB.split('_')[-1])

		if pvalueA>pvalueB:  #condition to remove A
			print "remove motif AAA",motifA
			motifstoremove[motifA]=1
			removeA=True
			continue
			
		else:
			print "remove",motifA,motifB
			motifstoremove[motifB]=1
		if removeA:
			continue
	'''for m in motifstoremove:
		print m,'\t',motifstoremove[m]
			#remove motifB:'''
	#remove the bad ones:
	for m in motifstoremove:
		del motifnames[m]

	print motifnames
	print len(motifnames)
	



	
	return 


if __name__=="__main__":
	main()