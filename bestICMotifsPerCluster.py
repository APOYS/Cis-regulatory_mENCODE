# for each of the cluster, pick out only the best IC motifs

"""
IN: memefile, clusterfile
OUT: memefile of the best IC motif per cluster
"""
import math
import scipy
from sys import argv



def calcAvgIC(pwm):
    """Calculates the average info content of each pwm"""
    bases = ['A', 'C', 'G', 'T']
    k = len(pwm['A'])
    ICs = [] 
    for pos in range(k):
        ic = 0
        for char in bases:
            if pwm[char][pos]!=0.0:
                ic += -pwm[char][pos]*math.log(pwm[char][pos],2)
            else:
                ic += 0.0
        #print pos, ic
        ICs += [2 - ic]
            
    #print ICs
    return scipy.mean(ICs)


def loadMEMEfile(filename):
    file=open(filename)
    seq=file.read().split("MOTIF")
    seq=seq[1:]
    motifs={}
    infos={}
    for s in range(len(seq)):
        t=seq[s].strip().split("\n")
        name=t[0].strip()
        motifs[name]=t[2:]
        infos[name]=t[0:2]
    for m in motifs:
        tdict={'A':[],'C':[],'G':[],'T':[]}
        for pos in range(len(motifs[m])):
            tmp=motifs[m][pos].strip().split("\t")
            #if len(tmp)!=6:
                #print "ERROR: Motif matrix does not contain 6 collumn. It is not typeEF." 
                #sys.exit(1)
            tdict['A']+=[float(tmp[0])]
            tdict['C']+=[float(tmp[1])]
            tdict['G']+=[float(tmp[2])]
            tdict['T']+=[float(tmp[3])]
            #tdict['E']+=[float(tmp[4])]
            #tdict['F']+=[float(tmp[5])]
        motifs[m]=tdict
    
    return motifs,infos

def printMEME(motif,info):
    print "MOTIF"+'\t'+info[0]
    print info[1]
    for pos in range(len(motif['A'])):
        line = []
        for char in ['A','C','G','T']:
            line += [str(motif[char][pos])]
        line = '\t'.join(line)
        print line
    return

def printMEMEtoString(motif,info,newname):
    returnstring = "MOTIF"+'\t'+newname
    returnstring += '\n' + info[1]
    for pos in range(len(motif['A'])):
        line = []
        for char in ['A','C','G','T']:
            line += [str(motif[char][pos])]
        line = '\t'.join(line)
        returnstring += '\n' + line
    return returnstring

def loadcluster(clustfile):

    clusters=[]
    for line in open(clustfile):
        tmp=line.strip().split()
        if len(tmp)<1:
            continue
        clusters+=[tmp]
    return clusters


def bestICmotifpercluster(clusters,motifs):
    bestICPerClust = []
    for i in range(len(clusters)):
        #print i
        c = clusters[i]

        bestICmotifs = []
        bestICscore = 0.0
        for m in c:
            ICscore = calcAvgIC(motifs[m])
            if ICscore > bestICscore:
                bestICscore = ICscore
                bestICmotifs = [m]
            elif ICscore == bestICscore:
                bestICmotifs += [m]
            else:
                continue
        bestICPerClust += [bestICmotifs]
    for i in range(len(bestICPerClust)):
        bestICPerClust[i] = bestICPerClust[i][0]
    return bestICPerClust



#testing 
memefile = argv[1] #"../motifClustering_3.0/method1_withDMV/motifs/All.Runs.mark.full.DMV.meme.renamed"
clusterfile = argv[2] #"../motifClustering_3.0/method1_withDMV/motifs/All.Runs.mark.full.DMV.meme.renamed.0.15.L2.hclust"
outfile = argv[3]

motifs, infos = loadMEMEfile(memefile)
clusters = loadcluster(clusterfile)

bestICPercluster = bestICmotifpercluster(clusters,motifs)

# now print out the results to MEME file
out = open(outfile,'w')
header = """MEME version 4.5

ALPHABET= ACGT

strands: +

Background letter frequencies (from
A 0.295 C 0.205 G 0.205 T 0.295

"""
out.write(header)


for i in range(len(bestICPercluster)):
    motifname = bestICPercluster[i]
    cname = "C"+str(i)+"_" + motifname
    #print cname # this is the name of the cluster now 
    stringtoprint = printMEMEtoString(motif=motifs[motifname],info=infos[motifname],newname=cname)
    #print stringtoprint
    out.write(stringtoprint+'\n\n')
out.close()
    
    
