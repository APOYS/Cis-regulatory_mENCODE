
from sys import argv


def main():
	memefile=argv[1]
	pvaluecutoff=float(argv[2])
	outfile=argv[3]


	motifs=open(memefile).read().split("MOTIF")
	header=motifs[0]
	motifs=motifs[1:]

	motifstoprint=[]

	for pwm in motifs:
	    name=pwm.strip().split('\n')[0]
	    #print pwm.split("_")[-1]
	    pvalue=float(name.split("_")[-1])
	    if pvalue<pvaluecutoff:
	        motifstoprint+=[pwm]
	out=open(outfile,'w')
	out.write(header)
	for pwm in motifstoprint:
	    out.write("MOTIF"+pwm)
	out.close()

	print len(motifstoprint)
	return

if __name__=="__main__":
	main()