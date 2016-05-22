"""
Input:  files:
		 1 is the input-normalized_coverage mark bed file (binned)
		 1 is the peak regions of the histone mark (binned)
		 1 is the score for each motif. 
Output:
Correlation between the motif and the histone mark 
"""
from sys import argv
from scipy import stats
def main():
	coveragefile=argv[1]
	scorefile=argv[2]
	peakfile=argv[3]
	
	peaks={}
	for line in open(peakfile).read().strip().split('\n'):
		tmp=line.strip().split('\t')
		chrom=tmp[0]
		start=tmp[1]
		try:
			peaks[chrom][start]=1
		except KeyError:
			peaks[chrom]={}
			peaks[chrom][start]=1

	scores_cov={}
	for line in open(scorefile).read().strip().split('\n'):
		tmp=line.strip().split('\t')
		s=float(tmp[1])
		name=tmp[0].split('_')
		chrom=name[0]
		loc=name[1]
		if chrom in peaks and loc in peaks[chrom]:
			try:
				scores_cov[chrom][loc]=[s,0]
			except KeyError:
				scores_cov[chrom]={}
				scores_cov[chrom][loc]=[s,0]
	for line in open(coveragefile).read().strip().split('\n'):
		tmp=line.strip().split('\t')
		cov=float(tmp[3])
		chrom=tmp[0]
		loc=tmp[1]
		if chrom in scores_cov and loc in scores_cov[chrom]:
			scores_cov[chrom][loc][1]=cov
	
	scorevector=[]
	covector=[]
	for chrom in scores_cov:
		for loc in scores_cov[chrom]:
			scorevector+=[scores_cov[chrom][loc][0]]
			covector+=[scores_cov[chrom][loc][1]]
	correlation=stats.spearmanr(scorevector, covector)
	print correlation

	return

if __name__=="__main__":
	main()