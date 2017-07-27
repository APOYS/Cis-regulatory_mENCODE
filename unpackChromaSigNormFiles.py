#!/usr/bin/env python


from sys import argv
import os
def main():
	"""  ONLY WORKS WITH mm10 !!!!!!!

	INPUT: chrom binfile, mm10 chromsizes, chromname,outfile

	OUTPUT: Standard output containing signal for 100bp bins
	"""

	binfile = argv[1]
	genomesize =  argv[2]
	chromname = argv[3]
	outfile = argv[4]
	chromsizes = {}
	for line in open(genomesize): 
		tmp = line.strip().split()
		chromsizes[tmp[0]] = int(tmp[1])/100 +1   #number of bins

	cmd = "/home/vungo/tools/bin2txttool/bin2txt %s 1 %s > %s" %(binfile, chromsizes[chromname],outfile)
	print cmd 
	os.system(cmd)

	#combine the result into a bedgraph file
	lines = open(outfile).readlines()
	out = open(outfile,'w')
	for i in range(chromsizes[chromname]-1):
		s = str(i*100)
		e = str((i +1) *100)
		line = chromname +'\t'+ s+'\t'+e+'\t'+lines[i]
		out.write(line)
	line = chromname +'\t'+ e+'\t'+str(chromsizes[chromname])+'\t'+lines[i]
	out.write(line)
	out.close()

if __name__ == "__main__":
	main()
			
