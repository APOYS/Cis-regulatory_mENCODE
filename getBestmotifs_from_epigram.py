"""
INPUT: fullmodel meme file. fisher p-value file (from epigram), p-value cutoff, enrichement cutoff

OUTPUT: best motifs according to the cutoffs in a .meme file
"""

from sys import argv

def main():
	#memefile=argv[1]
	#fisherfile=argv[2]
	#pvaluecutoff=float(argv[3])
	#enrichmentcutoff=float(argv[4])
	fisherfile="/Users/vungo/Downloads/fisher.pvalues.tsv"

	#read the fisher file:
	fishertable=[]
	for line in open(fisherfile):
		tmp=line.strip().split('\t')
		for i in range(3,len(tmp)):
			tmp[i]=float(tmp[i])
			#print tmp, tmp[6],tmp[8],i[6]/i[8]
		fishertable+=[tmp[1:2]+[tmp[3]]+[tmp[6]]+[tmp[8]]+[tmp[6]/tmp[8]]]
	for i in fishertable:
		if i[-1]>1.5:
			print i
		
	#add the enrichement to the table:



	return

if __name__=="__main__":
	main()