"""
IN: memefile
OUT:memefile without header
"""

from sys import argv

def main():
	infile=argv[1]
	outfile=argv[2]
	seqs=open(infile).read().strip().split("MOTIF")
	seqs=seqs[1:]
	seq="MOTIF"+"MOTIF".join(seqs)
	seq=seq.strip()
	if seq=="MOTIF":
		out=open(outfile,'w')
		out.write('')
		out.close()
	else:
		out=open(outfile,'w')
		out.write(seq)
		out.close()
	return

if __name__=="__main__":
	main()