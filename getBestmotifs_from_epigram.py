"""
INPUT: mark-epigram.meme file. fisher p-value file (from epigram), auc file, p-value cutoff, enrichement cutoff

OUTPUT: best motifs according to the cutoffs in a .meme file
"""

from sys import argv

def main():
	memefile=argv[1]
	fisherfile=argv[2]
	aucfile=argv[3]
	enrichmentcutoff=float(argv[4])
	outfile=argv[5]
	
	pvaluecutoff=1e-20


	#outfile="/Users/vungo/Downloads/epigramtest.bestmotifs.txt"
	#aucfile="/Users/vungo/Downloads/epigramtest.auc.txt"
	#fisherfile="/Users/vungo/Downloads/epigramtest.fisher.txt"
	
	#enrichmentcutoff=1.5
	#print pvaluecutoff
	#read the fisher file:
	fishertable=[]
	for line in open(fisherfile):
		tmp=line.strip().split('\t')
		for i in range(3,len(tmp)):
			tmp[i]=float(tmp[i])
			#print tmp, tmp[6],tmp[8],i[6]/i[8]
		if tmp[2]=="P":
			fishertable+=[tmp[1:2]+[tmp[3]]+[tmp[6]]+[tmp[8]]+[tmp[6]/tmp[8]]]
	
	motifstokeep=[]
	for i in fishertable:
		if i[-1]>enrichmentcutoff and i[1]<pvaluecutoff:
			#print i
			motifstokeep+=[i]
	aucscores={}
	for line in open(aucfile):
		tmp=line.strip().split('\t')
		aucscores[tmp[1]]=float(tmp[2])
	#print aucscores
	listofmotifs=[]
	
	for line in motifstokeep:
		if aucscores[line[0]]>0.5:
			#print line[0],line[1],line[-1],aucscores[line[0]]
			if line[1]==0:
				towrite=line[0].split('_')[0]+'_'+str('%.3f' %aucscores[line[0]])
				listofmotifs+=[towrite]
				#out.write(towrite+'\n')
			else:
				towrite=line[0].split('_')[0]+'_'+str('%.3f' %aucscores[line[0]])
				listofmotifs+=[towrite]
				#out.write(towrite+'\n')

	print "Number of good motifs",len(listofmotifs)
	motifs=open(memefile).read().split("MOTIF")
	header=motifs[0]
	motifs=motifs[1:]
	motifstoprint=[]
	
	for m in listofmotifs:
		for pwm in motifs:
			if m.strip() in pwm:
				motifstoprint+=[pwm]
	out=open(outfile,'w')
	out.write(header)
	for pwm in motifstoprint:
		out.write("MOTIF"+pwm)
	out.close()

	return

if __name__=="__main__":
	main()