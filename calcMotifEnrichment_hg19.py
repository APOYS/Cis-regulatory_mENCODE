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

args = parser.parse_args()

#taking inputs:
fileA = args.fileA
fileB = args.fileB
genome = args.genome
outA = args.outfileA
outB = args.outfileB


#converting the bedfiles into fasta

faAname = fileA +'.tmp.fa'
faBname = fileB + '.tmp.fa'


cmd1 = "bedtools getfasta -fi {} -bed {} -fo {}".format(genome, fileA,faAname)
cmd2 = "bedtools getfasta -fi {} -bed {} -fo {}".format(genome, fileB,faBname)

print cmd1
os.system(cmd1)
print cmd2
os.system(cmd2)

ssbA = faAname+'.ssb'
ssbB = faBname+'.ssb'

cmd3 = "perl ssb.pl {} {} {} {}".format(faAname,faBname, ssbA, ssbB)

print cmd3
os.system(cmd1)




