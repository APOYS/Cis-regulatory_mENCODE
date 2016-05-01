from sys import argv
import random as rd
num=argv[1]
filename=argv[2]
output=argv[3]

seqs=open(filename).read().strip().split("\n")

numseqs=len(seqs)
if int(num)==0: #take 10% from the input
	print "taking 10% of", len(seqs)
	num=int(0.1*len(seqs))
toprintseqs=rd.sample(seqs,int(num))
out=open(output,'w')
for seq in toprintseqs:
	out.write(seq+"\n")
out.close()
