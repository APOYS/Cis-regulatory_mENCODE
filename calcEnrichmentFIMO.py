
"""
IN: Positive FIMO result, DS FIMO result, fasta file, out file

OUT: enrichemtns of the motifs in the sequences. 
"""

from sys import argv
from scipy.stats import stats

def main():
	posfile = argv[1]
	negfile = argv[2]
	fastafile = argv[3]
	outfile = argv[4]


	totalseq = len(open(fastafile).read().split(">"))-1
	posdict = {}
	file = open(posfile)
	file.readline()
	for line in file:
		tmp = line.strip().split('\t')
		if tmp[0] not in posdict:
			posdict[tmp[0]] = {}
		posdict[tmp[0]][tmp[1]] = 1 

	negdict = {}
	file = open(negfile)
	file.readline()
	for line in file:
		tmp = line.strip().split('\t')
		if tmp[0] not in negdict:
			negdict[tmp[0]] = {}
		negdict[tmp[0]][tmp[1]] = 1 

	
	lines = [] 
	pvalues = [] 
	for motif in posdict:
		if motif not in negdict:
			print "ERROR, not the same set of motifs"
			break
		posnum = len(posdict[motif])
		negnum = len(negdict[motif])
		enrichment, pvalue = stats.fisher_exact([[posnum, totalseq - posnum], [negnum, totalseq - negnum]])
		pvalues += [pvalue]
		line = [motif, str(posnum), str(totalseq - posnum), str(negnum), str(totalseq - negnum), str(enrichment), str(pvalue)]
		line = '\t'.join(line)
		lines += [line]
	
	sortedindex = sorted(range(len(pvalues)), key = lambda x: pvalues[x], reverse = True)
	lines = [lines[x] for x in sortedindex]
	target = open(outfile,'w')
	for line in lines:
		target.write(line+'\n')
	target.close()

	return



if __name__=="__main__":
	main()