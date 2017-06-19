from sys import argv

def main():
	infile = argv[1]
	k = int(argv[2])
	outfile = argv[3]

	target = open(outfile,'w')
	lines = open(infile).read().split('\n')
	for line in lines:
		if "snpID" in line:
			continue

		tmp = line.split('\t')
		if len(tmp)<2:
			continue
		chrom = tmp[0]
		if chrom =="chr23":
			chrom = "chrX"
		elif chrom =="chr24":
			chrom = "chrY"
		loc = int(tmp[1])
		s = loc - k
		e = loc + k 
		newline = chrom +'\t' + str(s)+'\t'+str(e)
		target.write(newline+'\n')
	target.close()
	return

if __name__=="__main__":
	main()
