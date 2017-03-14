"""
IN: Take the X.Summary.tsv file and 

OUT: produce a more complete file with SNP locations
"""


from sys import argv

def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)
def revcom(s):
    return complement(s[::-1])


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
		#print tmp
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
		refstrand = tmp[4]
		snpstrand = tmp[8]
		#print refstrand,refseq,snpstrand,snpseq

		if refstrand == "-":
			refseq = revcom(refseq.upper())
		if snpstrand =="-":
			snpseq = revcom(snpseq.upper())
		#print refseq,snpseq
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