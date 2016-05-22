"""
INPUT: A bedfile f, a binsize n
OUTPUT: a bedfile that was binned by size n
"""

from sys import argv
def main():
	input=argv[1]
	n=int(argv[2])
	output=argv[3]
	#read bedfile
	seqs=open(input).read().strip().split('\n')
	out=open(output,'w')
	for line in seqs:
		tmp=line.strip().split('\t')
		chrom=tmp[0]
		start=(int(tmp[1])-n/2)/500*500
		end=(int(tmp[2])+n/2)/n*n
		newline=chrom+'\t'+str(start)+'\t'+str(end)
		out.write(newline)
	out.close()
	return

if __name__=="__main__":
	main()