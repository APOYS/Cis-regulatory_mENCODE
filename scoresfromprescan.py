from sys import argv
bedfile=argv[1]
prescan=argv[2]
outfile=argv[3]


bed=open(bedfile).read().strip().split('\n')
tmp=open(prescan).read().strip().split('\n')
tmp[:2]
scoredict={}
for line in tmp:
    t=line.split()
    try:
        scoredict[t[0]]=float(t[1])
    except:
        print t


target=open(outfile,'w')
for region in bed:
    tmp =region.split("\t")
    chrom=tmp[0]
    start=int(round(float(tmp[1])/100)*100)
    end=int(round(float(tmp[2])/100)*100)
    maxscore=0
    maxname=""
    while start<end:
        name=chrom+'_'+str(start)+"_0.1"
        try:
            s=scoredict[name]
        except KeyError:
            s=0
        #print start,end,s
        start+=100
        if s>=maxscore:
            maxscore=s
            maxname=name
    target.write(maxname+'\t'+str(maxscore)+'\n')
target.close()
