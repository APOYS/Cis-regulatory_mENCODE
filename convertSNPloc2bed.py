"""
IN: snploc file, k
OUT: bed file containng loci from the snp +/- k 
snp loc file is in this format :

snp	chr	pos
snp_ACC_1	chr1	877830
....

"""

from sys import argv

def main():

	infile = argv[1]
	k = int(argv[2])
	outfile = argv[3]

	file = open(infile)
	file.readline()

	out = open(outfile,'w')
	for line in file:
		line = line.strip().split('\t')
		chrom = line[1]
		start = str(int(line[2]) - k)
		end = str(int(line[2]) + k)
		nl = chrom+'\t'+start+'\t'+end
		out.write(nl+'\n')
	out.close()


	return



if __name__ == "__main__":
    main()
