"""
IN: a meme file. A prefix to add to infront of each motif

OUT: a meme file with renamed motifs
"""

from sys import argv

def main():
	infile=argv[1]
	prefix=argv[2]
	outfile=argv[3]
	seq=open(infile).read().strip()
	seq=seq.replace("MOTIF\t","MOTIF\t"+prefix)
	out=open(outfile,'w')
	out.write(seq)
	out.close()
	return

if __name__=="__main__":
	main()