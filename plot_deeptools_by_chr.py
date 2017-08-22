#!/bin/env python
import argparse
import os
import time, threading
 




def main():
	"""This function takes a directory of conservation-tagged motif loci (bedformat) then:
	- shuffle each of the file then put 5000 regions in another file in the output directory
	- Combine those files into categories : Con.Same, Con.Similar, Con.Different, Uncon, and JustCon, with histone marks
	- remove the tmp 5000 regions files
	- For each of the category, make a deeptool plot

	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--inDir", help="input directory, containing motif loci in BED format")
	parser.add_argument("-o", "--outDir", help="output directory")
	parser.add_argument("-bw", "--bigwigfile", help="bigwigfile")
	parser.add_argument("-g", "--genome", help="indicate the reference genome: hg19 or mm10")

	args = parser.parse_args()

	inDir = args.inDir
	outDir = args.outDir
	bwFile = args.bigwigfile
	genome = args.genome
	chromlist = []
	if genome == "hg19":
		chromlist = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10",
		"chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20",
		"chr21","chr22","chrX","chrY"]
	elif genome == "mm10":
		chromlist = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10",
		"chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chrX","chrY"]
	else:
		print "ERROR, please specify the genome"

	tmp = """#!/bin/bash
#$ -cwd
#$ -pe smp 1 ##using 1 core
#$ -j y
#$ -S /bin/bash
#$ -V

#cd YOURDIR
"""

	#read the files in the input dir
	# make the random regions
	
	numinputfiles = 0
	inFiles = os.listdir(inDir)
	for file in inFiles:
		if "qsub" in file:
			continue
		numinputfiles += 1
		outqsubfile = open(inDir+'/'+file+".plotdeep.qsub",'w')

		
		cmd = """grep -P 'CHROM\t' INFILE| cut -f1,2,3|shuf|head -5000 >OUTFILE"""
		infile = inDir+'/'+file
		content = tmp.replace("YOURDIR",'wd')

		for chrom in chromlist:
			outfile = outDir+'/'+file +'.'+chrom+'.5000'
			newcmd = cmd.replace("CHROM",chrom).replace("INFILE",infile).replace("OUTFILE",outfile)
			content += newcmd +'\n'

		outqsubfile.write(content)
		outqsubfile.close()

	for file in os.listdir(inDir):
		if ".plotdeep.qsub" in file:
			os.system("qsub "+inDir+file)


	#wait until all the result files are in outDir

	while True:
		print "Checking if all the files are in outDir"
		numresultfiles = 0
		for file in os.listdir(outDir):
			if "chr" in file and "H3K" in file:
				numresultfiles += 1
			if numresultfiles == len(chromlist)*numinputfiles:
				print "All files are here. Proceeed..."
				break
			else:
				print "keep waiting..."
				time.sleep(30)

	return







if __name__=="__main__":
	main()