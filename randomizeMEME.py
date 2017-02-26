import random as rd
from sys import argv


def load_MEME(filename):
    file=open(filename)
    seq=file.read().split("MOTIF")
    header = seq[0]
    seq=seq[1:]
    motifs={}
    infos={}
    for s in range(len(seq)):
        t=seq[s].strip().split("\n")
        name=t[0]
        motifs[name]=t[2:]
        infos[name]=t[0:2]
    for m in motifs:
        tdict={'A':[],'C':[],'G':[],'T':[]}
        for pos in range(len(motifs[m])):
            if "URL" in motifs[m][pos]:
                continue
            tmp=motifs[m][pos].strip().split("\t")
            tdict['A']+=[float(tmp[0])]
            tdict['C']+=[float(tmp[1])]
            tdict['G']+=[float(tmp[2])]
            tdict['T']+=[float(tmp[3])]
            #tdict['E']+=[float(tmp[4])]
        motifs[m]=tdict
    
    return motifs,infos,header 


# for each motif, print it in a random fashion

def main():
    infile = argv[1]
    outfile = argv[2]
    motifs, infos,header = load_MEME(infile)

    #print header

    target = open(outfile,'w')
    target.write(header)

    for m in motifs:
        pwm = motifs[m]
        info = infos[m]
        order = range(len(pwm['A']))
        randomorder = rd.sample(order,len(order))
        #print '\n'.join(info)
        content = '\n'.join(info)
        for pos in randomorder:
            charrandomorder = rd.sample(pwm.keys(),len(pwm.keys()))
            line = []
            for base in charrandomorder:
                line += [str(pwm[base][pos])]
            line = '\t'.join(line)
            #print line
            content += '\n'+line
        target.write(content +'\n\n')

    target.close()
    return 


if __name__=="__main__":
    main()