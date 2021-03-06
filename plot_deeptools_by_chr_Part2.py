"""This file takes a directory of con, uncon etc combined files  and makes qsub files for compute matrix and plot

"""
import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inDir", help="input directory, containing combined motif loci in BED format")
parser.add_argument("-bw", "--bigwigfile", help="bigwigfile")
parser.add_argument("-rd","--randomBedfile", help = "BED file contains random regions")
args = parser.parse_args()


inDir = args.inDir
bigwigfile = args.bigwigfile
randomBedfile = args.randomBedfile

for file in os.listdir(inDir):
	if os.stat(inDir+file).st_size == 0:
		print "Empty, remove file", file
		os.system("rm "+inDir+'/'+file)
	if "Con.H3K" in file and "qsub" not in file and ".gz" not in file and ".eps" not in file and "JustCon" not in file:
		cmd = "mv %s %s" %(file,file.replace("Con.H3K","JustCon.H3K"))
		os.system(cmd)



computeMatrixTemplate = """#!/bin/bash
#$ -cwd
#$ -pe smp 1 ##using 1 core
#$ -j y
#$ -S /bin/bash
#$ -V

computeMatrix reference-point -S BIGWIG -R REGIONS RANDOMFILE -out OUTPUT --referencePoint=center -a 2500 -b 2500
"""


types = ["Con.Same","Con.Different","Con.Similar","Uncon","JustCon"]
marks = ["H3K4me1","H3K4me3","H3K9me3","H3K27me3","H3K27ac","H3K36me3"]

files = [inDir + x for x in os.listdir(inDir)]
for type in types:
	qsubfile = open(type+".qsub",'w')
	regionfiles = ''

	for mark in marks:
		#get the regions 
		for file in files:
			if type in file and mark in file and ".gz" not in file and ".qsub" not in file and ".eps" not in file:
				regionfiles += file +' '

	outputfile = type+'.'+mark+'.'+bigwigfile.split('/')[-1]+'.gz'
	content  = computeMatrixTemplate.replace("BIGWIG", bigwigfile).replace("REGIONS",regionfiles).replace("RANDOMFILE",randomBedfile).replace("OUTPUT",outputfile)
	#print content
		
	qsubfile.write(content)
	qsubfile.close()



