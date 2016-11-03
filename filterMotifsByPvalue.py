"""This method filters for motifs based on their auc and pvalues.

IN: meme file to filter, auc cutoff, pvalue cutoff

OUT: filtered file based on auc and pvalue

"""

from sys import argv

def main():
	infile = argv[1]
	aucthreshold = float(argv[2])
	pvalthreshold = float(argv[3])
	outfile = argv[4]

	print "Filtering ",infile
	print "AUC threshold is",aucthreshold
	print "P-value threshold is",pvalthreshold

	motifs=open(infile).read().strip().split("MOTIF")
	motifs=motifs[1:]

	filteredMotifs=[]

	for m in motifs:
	    name=m.split('\n')[0].strip().split("_")
	    pval=float(name[-1])
	    auc=float(name[-2])
	    if auc >=aucthreshold and pval <= pvalthreshold:
	        filteredMotifs+=[m]

	print "Started with",len(motifs)
	print "Ends with",len(filteredMotifs)

	target = open(outfile,'w')
	newseq = "MOTIF".join(filteredMotifs)
	target.write(newseq)
	target.close()


	return 

if __name__=="__main__":
	main()