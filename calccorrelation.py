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
		scoredict[chrom+'_'+loc]=s
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
	for file in coveragefiles[:10]:
		print file
		coveragedict=readcoveragefromfile(coveragedir+'/'+file)
		coverages[file]=coveragedict
	
	output=open("Spearman_correlation_motif_histone.tsv")
	for file in scorefiles[:5]:
		print file,"read scores"
		scores=readscorefromfile(scorefiledir+'/'+file)
		print "get vectors"
		
		for coveragedict in coverages:
			scorevector=[]
			covector=[]
			for name in coverages[coveragedict]:
				try:
					scorevector+=[scores[name]]
					covector+=[coverages[coveragedict][name]]
				except KeyError:
					pass
			correlation=stats.spearmanr(scorevector, covector)
			line=file+'\t'+coveragedict+'\t'+str(correlation[0])+'\t'+str(correlation[1])
			print line
			output.write(line+'\n')
	output.close()

	return

if __name__=="__main__":
	main()
