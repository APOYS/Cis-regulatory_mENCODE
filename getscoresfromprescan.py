import os
from sys import argv

'''Usag: Command bedlink outdir'''

def loadscannedresult(filelink):
    tmp=open(filelink).read().strip().split('\n')
    tmp[:2]
    scoredict={}
    for line in tmp:
        t=line.split()
        try:
            scoredict[t[0]]=float(t[1])
        except:
            print t
    return scoredict

def outputscannresult(bedfile,scoredict,outputdir,motif):
    #scoredict is the dict that contains the scores for the motif at each of its genomic locations
    bed=open(bedfile).read().strip().split('\n')
    binsize=500
    target=open(outputdir+"/"+motif,'w')
    for region in bed:
        tmp =region.split("\t")
        chrom=tmp[0]
        if "X" in chrom or "Y" in chrom or "M" in chrom:
            continue
        start=-1
        end=-1
        try:
            start=int(round(float(tmp[1])/binsize)*binsize)
            end=int(round(float(tmp[2])/binsize)*binsize)
        except:
            print 'error in start end',tmp
            pass
        while start<end:
            name=chrom+'_'+str(start)+"_0.5"
            s="None"
            s=scoredict[name]
            start+=binsize
            target.write(name+'\t'+str(s)+'\n')

    target.close()
    return

bedlink=argv[1]
outdir=argv[2]

prefix='/home/vungo/Epigram_project/MouseENCODE/WorkingDCCdata/Regions_forscanning/Motifs_reformatedforscanning/'
L=os.listdir(prefix)
#print L
resultfiles=[]
for i in L:
    if 'scanned' in i: 
        resultfiles+=[i]
print len(resultfiles),resultfiles[0]

os.system("mkdir "+outdir)
for motif in resultfiles:
    #motif="8_motif.101_Lung_E16.5_H3K36me3169_0.516_9.978677e-16_14.motif.scanned"
    print motif
    scoredict=loadscannedresult(prefix+motif)
    if len(scoredict)==0:
        print "NO scores"
        continue
    print "Done loading... Now writing..."
    outputscannresult(bedlink,scoredict,outdir,motif)
