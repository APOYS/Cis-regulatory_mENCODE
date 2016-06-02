"""
IN: a meme file. A prefix to add to infront of each motif

OUT: a meme file with renamed motifs
"""

from sys import argv

def main():
	infile=argv[1]
	prefix=argv[2]
	outfile=argv[3]
	seqs=open(infile).read().strip().split('\n')
	out=open(outfile,'w')
	for line in seqs:
		tmp=line.strip()
		if "MOTIF" in line:
			tmp2=line.replace("MOTIF",'').strip()
			tmp="MOTIF\t"+prefix+'_'+tmp2
		out.write(tmp+'\n')
	out.close()
	return

if __name__=="__main__":
	main()