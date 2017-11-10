import argparse
import os

'''
This script takes 2 bed files, 
make the fasta files;
do Sequence-set-balancing on them, 
then scan the files using kais method

'''

#parsing input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--fileA", help="input first bed file")
parser.add_argument("-b", "--fileB", help="input second bed file")
parser.add_argument("-g", "--genome", help="genome file in fasta format")
parser.add_argument("-oa", "--outfileA", help="name of output for file A")
parser.add_argument("-ob", "--outfileB", help="name of output for file B")
parser.add_argument("-m","--motiffile", help = "motif file in MEME format")

args = parser.parse_args()

#taking inputs:
fileA = args.fileA
fileB = args.fileB
genome = args.genome
outA = args.outfileA
outB = args.outfileB
motiffile = args.motiffile


#converting the bedfiles into fasta

faAname = fileA +'.tmp.fa'
faBname = fileB + '.tmp.fa'


cmd1 = "bedtools getfasta -fi {} -bed {} -fo {}".format(genome, fileA,faAname)
cmd2 = "bedtools getfasta -fi {} -bed {} -fo {}".format(genome, fileB,faBname)

print cmd1
os.system(cmd1)
print cmd2
os.system(cmd2)

ssbA = fileA.replace(".bed",'.fa.ssb')
ssbB = fileB.replace(".bed",'.fa.ssb')

cmd3 = "perl ssb.pl {} {} {} {}".format(faAname,faBname, ssbA, ssbB)

print cmd3
#os.system(cmd3)



# get the Bedfile back from the ssb fa files

ssbBedA = open(ssbA+'.BED','w')
for line in open(ssbA):
	if line.startswith(">"):
		tmp = line.strip().split(":")
		chrom = tmp[0].replace(">",'')
		s,e = tmp[1].split('-')
		newline = '\t'.join([chrom,s,e])
		ssbBedA.write(newline + '\n')
ssbBedA.close()

ssbBedB = open(ssbB+'.BED','w')
for line in open(ssbB):
	if line.startswith(">"):
		tmp = line.strip().split(":")
		chrom = tmp[0].replace(">",'')
		s,e = tmp[1].split('-')
		newline = '\t'.join([chrom,s,e])
		ssbBedB.write(newline + '\n')
ssbBedB.close()



print "Scanning ..."
print "Foreground"

genomeindex = "/home/vungo/MouseENCODE_project/Kaisscripts/hg19.idx"
cmd4 = "/home/vungo/MouseENCODE_project/Kaisscripts/motifscan {} {} {} {}".format(genomeindex, motiffile, ssbBedA, outA)
print cmd4
os.system(cmd4)
print "Background"
print cmd5
cmd5 = "/home/vungo/MouseENCODE_project/Kaisscripts/motifscan {} {} {} {}".format(genomeindex, motiffile, ssbBedB, outB)
os.system(cmd5)




