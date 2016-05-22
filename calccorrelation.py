"""
Input:  files:
		 1 is the input-normalized_coverage mark bed file (binned)
		 all the peak regions of each tissue-stage (binned)
		 1 is the score for each motif. 
Output:
Correlation between the motif and the histone mark 
"""
import os
from sys import argv
from scipy import stats
def readscorefromfile(file):
	scoredict={}
	for line in open(file):
		tmp=line.strip().split('\t')
		s=float(tmp[1])
		name=tmp[0].split('_')
		chrom=name[0]
		loc=name[1]
		scoresdict[chrom+'_'+loc]=s
	return scoredict
def readcoveragefromfile(file):
	coveragedict={}
	for line in open(file):
		tmp=line.strip().split('\t')
		cov=float(tmp[1])
		name=tmp[0]
		coveragedict[name]=cov
	return coveragedict
def main():
	coveragedir=argv[1]
	scorefiledir=argv[2]
	coveragefiles=[]
	for file in os.listdir(coveragedir):
		if "filtered" in file and "bin500" in file:
			coveragefiles+=[file]
	
	scorefiles=[]
	for file in os.listdir(scorefiledir):
		if "scanned" in file and "motif" in file:
			scorefiles+=[file]
	

	print "read covs"
	coverages={}
	for file in coveragefiles:
		print file
		coveragedict=readcoveragefromfile(coveragedir+'/'+file)
		coverages[file]=coveragedict
	

	for file in scorefiles:
		print file,"read scores"
		scores=readscorefromfile(scorefiledir+'/'+file)
		print "get vectors"
		scorevector=[]
		covector=[]
		for coveragedict in coverages:
			for name in coverages[coveragedict]:
				scorevector+=[scores[name]]
				covector+=[coverages[coveragedict][name]]
				correlation=stats.spearmanr(scorevector, covector)
				print file+'\t'+coveragedict+str(correlation)
	'''print "read Peaks"
	peaks={}
	for line in open(peakfile):
		tmp=line.strip().split('\t')
		chrom=tmp[0]
		start=tmp[1]
		try:
			peaks[chrom][start]=1
		except KeyError:
			peaks[chrom]={}
			peaks[chrom][start]=1
	'''
	return

if __name__=="__main__":
	main()
