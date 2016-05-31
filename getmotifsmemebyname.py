"""
IN: a list of motifs will be taken from the meme file

OUT: a meme file with just the motifs listed. 
"""
from sys import argv
def main():
	memefile=argv[1]
	motiflist=argv[2]
	outfile=argv[3]

	motifs=open(memefile).read().split("MOTIF")
	header=motifs[0]
	motifs=motifs[1:]
	listofmotifs=open(motiflist).read().strip().split('\n')
	
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