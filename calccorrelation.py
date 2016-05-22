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
def readcoveragefromfile(file,peakfile):
	peakdict={}
	for line in open(peakfile):
		tmp=line.strip().split('\t')
		name=tmp[0]+'_'+tmp[1]
		peakdict[name]=1

	coveragedict={}
	for line in open(file):
		tmp=line.strip().split('\t')
		cov=float(tmp[1])
		name=tmp[0]
		if name in peakdict:
			coveragedict[name]=cov
	return coveragedict
def main():
	coveragedir=argv[1]
	scorefiledir=argv[2]
	outfile=argv[3]
	start=int(argv[4])
	end=int(argv[5])
	peakdir=argv[6]
	coveragefiles=[]
	for file in os.listdir(coveragedir):
		if "filtered" in file and "bin500" in file:
			coveragefiles+=[file]
	
	scorefiles=[]
	for file in os.listdir(scorefiledir):
		if "scanned" in file and "motif" in file:
			scorefiles+=[file]
	print "READING",end-start,"SCORE FILES"
	for file in scorefiles[start:end]:
		print file
	

	print "read covs"
	coverages={}
	for file in coveragefiles:
		print file
		peakfile=peakdir+'/'+file.split(".bin500")[0]+".DCC.mark.bin500.bed"
		#peakfile=peakfile.replace("facial","Facial")
		#peakfile=peakfile.replace("tube","Tube")
		try:
			coveragedict=readcoveragefromfile(coveragedir+'/'+file,peakfile)
		except IOError:
			pass

		coverages[file]=coveragedict
	
	output=open(outfile,'w')
	print "READING",end-start,"SCORE FILES"
	for file in scorefiles[start:end]:
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
