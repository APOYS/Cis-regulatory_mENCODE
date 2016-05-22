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
	if len(seqs)==0:
		print "Empty file, exit"
		sys.exit(0)
	out=open(output,'w')
	for line in seqs:
		tmp=line.strip().split('\t')
		chrom=tmp[0]
		start=(int(tmp[1])-n/2)/500*500
		end=(int(tmp[2])+n/2)/n*n
		numberofbins=(end-start)/500
		for i in range(numberofbins):
			s=start+i*500
			e=start+(i+1)*500
			newline=chrom+'\t'+str(s)+'\t'+str(e)
			out.write(newline+'\n')
	out.close()
	return

if __name__=="__main__":
	main()