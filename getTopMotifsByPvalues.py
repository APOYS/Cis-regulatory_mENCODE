"""This method filters for top k percent motifs based on their auc and pvalues.

IN: meme file to filter, auc cutoff, pvalue cutoff

OUT: filtered file based on auc and pvalue

"""

from sys import argv

def main():
	infile = argv[1]
	k = float(argv[2])
	outfile = argv[3]

	print "Filtering ",infile
	print "Number of motifs to keep", k 
	#print "AUC threshold is",aucthreshold
	#print "P-value threshold is",pvalthreshold

	motifs=open(infile).read().strip().split("MOTIF")
	motifs=motifs[1:]

	numberofmotifs=int(len(motifs)*k)
	pvalues=[]

	for m in motifs:
	    name=m.split('\n')[0].strip().split("_")
	    pval=float(name[-1])
	    #auc=float(name[-2])
	    #if auc >=aucthreshold and pval <= pvalthreshold:
	    #    filteredMotifs+=[m]
	    pvalues += [pval]


	#sort the pvalues
	si = sorted(range(len(pvalues)), key=lambda k: pvalues[k],reverse=False)  #sort by pvalues, get the index
	#then reorder the other arrays based on that index
	motifs = [motifs[i] for i in si]
	
	target = open(outfile,'w')
	newseq = "MOTIF"+"MOTIF".join(motifs[:numberofmotifs])
	target.write(newseq)
	target.close()


	return 

if __name__=="__main__":
	main()