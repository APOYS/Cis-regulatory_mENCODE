"""
Input:  files:
		 1 is the input-normalized_coverage mark bed file (binned)
		 1 is the peak regions of the histone mark (binned)
		 1 is the score for each motif. 
Output:
Correlation between the motif and the histone mark 
"""
import time



from sys import argv
from scipy import stats
def main():
	coveragefile=("./WorkingDCCdata/DCC_regions_bin500/test/Cranio-Facial_E11.5.test.bed")
	scorefile=("./WorkingDCCdata/Regions_forscanning/Scanning_results/0_motif.100_Forebrain_E13.5_H3K4me162_0.503_7.785084e-24_12.motif.scanned")
	peakfile=("./WorkingDCCdata/DCC_regions_bin500/Cranio-Facial_E11.5_H3K27ac.DCC.narrowPeaks.mark.bin500.bed")
	print "read Peaks"
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
	
	start = time.time()
	print("hello")
	
	print "read scores"
	scores_cov={}
	for line in open(scorefile):
		tmp=line.strip().split('\t')
		s=float(tmp[1])
		name=tmp[0].split('_')
		chrom=name[0]
		loc=name[1]
		if chrom in peaks and loc in peaks[chrom]:
			scores_cov['_'.join(name)]=[s,0]
	
	end = time.time()
	print(end - start)
	start = time.time()
	print("hello")
	print "read covs"
	for line in open(coveragefile):
		tmp=line.strip().split('\t')
		cov=float(tmp[1])
		chrom=tmp[0]
		loc=tmp[1]
		name=chrom+'_'+loc
		if  name in scores_cov:
			scores_cov[name][1]=cov
	end = time.time()
	print(end - start)
	print "get vectors"
	scorevector=[]
	covector=[]
	for name in scores_cov:
		scorevector+=[scores_cov[name][0]]
		covector+=[scores_cov[name][1]]
	print "calc corl"
	correlation=stats.spearmanr(scorevector, covector)
	print correlation

	return

if __name__=="__main__":
	main()
end = time.time()
print(end - start)