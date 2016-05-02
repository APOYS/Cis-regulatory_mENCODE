"""
This script processes the files from the mENCODE project for Epigram for work with
Execute this in /resource/mEncode/ChIP-seq/bed_peaks
"""
import os
from sys import argv

"""This part filters for only REPLICATED peak files"""

file=argv[1]
#currentsortedfolder=argv[2]

#get the first line of the file only to get the metadata file
os.system("head -1 "+file + " > metadata.download.txt")
#download the metadata.tsv file
os.system("xargs -n 1 curl -O -L < metadata.download.txt")

os.system("grep replicated metadata.tsv > metadata.replicatedOnly.txt")
metadata=open("metadata.replicatedOnly.txt").read().strip().split('\n')

replicatedFiles=[]
for line in metadata:
	replicatedFiles+=[line.strip().split('\t')[0]]
print "Numer of replicated peak files is ",len(replicatedFiles)

#make the download link list for just the replicated files
allFiles=open(file).read().strip().split('\n')
linkstokeep=[]
for line in allFiles:
	name=line.split('/')[-1].replace('.bed.gz','')
	if name in replicatedFiles:
		linkstokeep+=[line]
print "Number of links to keep is",len(linkstokeep)

out=open("filestodownload.txt",'w')
for line in linkstokeep:
	out.write(line+'\n')
out.close()
os.system("mkdir tmp_new_download")
#os.chdir("tmp_new_download") 
#download all the files in the file to download
os.system("xargs -n 1 curl -O -L < filestodownload.txt")

#unzip them all
os.system("gunzip -f *.gz")

#move them all to the tmp folder
os.system("mv *.bed tmp_new_download")





