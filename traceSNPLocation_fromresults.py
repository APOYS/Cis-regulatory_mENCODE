"""
IN: Take the X.Summary.tsv file and 

OUT: produce a more complete file with SNP locations
"""


from sys import argv

def main():
	infile = argv[1]
	outfile = argv[2]
	#outfile = "../X.All.test.tsv"#argv[2]
	#infile = "../X.AllMotifs.Summary.tsv"
	target = open(outfile,'w')

	#read infile 
	lines = open(infile).read().strip().split('\n')
	header = lines[0]
	lines = lines[1:]

	target.write(header+'\t'+"SNPloc"+'\n')
	for line in lines:
		tmp = line.split('\t')
		print tmp
		seq = tmp[1]
		#seqsplit = seq.split(':')
		chrom = seq.split(':')[0]
		loc = seq.split(':')[1]
		#print loc
		#print seqsplit
		start = int(loc.split('-')[0])
		end = int(loc.split('-')[1])
		#print chrom,start,end
		refseq = tmp[7]
		snpseq = tmp[11]
		snploc = 0
		for i in range(len(refseq)):
			if refseq[i]!=snpseq[i]:
				#print i
				snploc = start + i
				break
		#print refseq,snpseq,snploc
		newline = '\t'.join(tmp)+'\t'+chrom+'_'+str(snploc)
		target.write(newline+'\n')
	target.close()


	return

if __name__=="__main__":
	main()