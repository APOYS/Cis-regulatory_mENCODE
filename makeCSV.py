import os
from scipy import stats
import numpy as np
from sys import argv

def loadvector(infile):
    seq=open(infile).read().strip().split('\n')
    vector=[]
    for line in seq:
        vector+=[float(line.split('\t')[1])]
    return vector

resultdir=argv[1]
print "reading from",resultdir
#resultdir="WorkingDCCdata/Regions_forscanning/TissueMarkPeaks100seqs/"
outfile=resultdir.replace('/',' ').strip().split(' ')[-1]+".csv"
print "output file to",outfile
prefix=resultdir
scorefiles=os.listdir(prefix)

names={}
for f in scorefiles:
    names[int(f.split('_')[0])]=f

scorematrix=[]   
for motif in sorted(names.keys()):
    #print motif
    vector=loadvector(prefix+names[motif])
    scorematrix+=[vector]

scorematrix=np.array(scorematrix)

target=open("/home/vungo/Epigram_project/MouseENCODE/WorkingDCCdata/Regions_forscanning/TissueMarkPeaks100seqs/"+outfile,'w')
for i in range(len(names)):
    print i
    line=[]
    for j in range(len(names)):
        line+=[str(stats.spearmanr(scorematrix[i],scorematrix[j])[0])]
    line='\t'.join(line)
    target.write(line+'\n')
target.close()
