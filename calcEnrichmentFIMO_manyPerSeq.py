
"""
IN: Positive FIMO result, DS FIMO result, out file

OUT: enrichemtns of the motifs in the sequences. The matches are counted directly, not just one per seq.
"""

from sys import argv
from scipy.stats import stats

def main():
	posfile = argv[1]
	negfile = argv[2]
	#fastafile = argv[3]
	outfile = argv[3]


	#totalseq = len(open(fastafile).read().split(">")) - 1
	posdict = {}
	file = open(posfile)
	file.readline()
	for line in file:
		tmp = line.strip().split('\t')
		if tmp[0] not in posdict:
			posdict[tmp[0]] = {}
		if tmp[1] not in posdict[tmp[0]]:
			posdict[tmp[0]][tmp[1]] = 1 
		else:
			posdict[tmp[0]][tmp[1]] += 1

	negdict = {}
	file = open(negfile)
	file.readline()
	for line in file:
		tmp = line.strip().split('\t')
		if tmp[0] not in negdict:
			negdict[tmp[0]] = {}
		if tmp[1] not in negdict[tmp[0]]:
			negdict[tmp[0]][tmp[1]] = 1 
		else:
			negdict[tmp[0]][tmp[1]] += 1

	
	lines = [] 
	pvalues = [] 
	#enrichments = []
	motifs = posdict.keys()
	for m in negdict:
		if m not in motifs:
			motifs += [m]
	for motif in motifs:
		negcount = 0
		poscount = 0
		if motif not in negdict:
			negcount = 0
		elif motif not in posdict:
			poscount = 0
		else:
			poscount = posdict[motif]
			negcount = negdict[motif]

		if negcount != 0:
			enrichment = float(poscount)/negcount
		else: 
			enrichment = "inf"
		
		#enrichments = [enrichment]
		line = [motif, str(poscount), str(negcount), str(enrichment)]
		line = '\t'.join(line)
		lines += [line]
	
	#sortedindex = sorted(range(len(pvalues)), key = lambda x: pvalues[x])
	#lines = [lines[x] for x in sortedindex]
	target = open(outfile,'w')
	for line in lines:
		target.write(line+'\n')
	target.close()

	return



if __name__=="__main__":
	main()