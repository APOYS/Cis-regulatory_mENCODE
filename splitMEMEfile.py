"""
IN: MEMEfile, number of subfile k
OUT: k subfiles 
"""
import argparse
from sys import argv





def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--memefile", help="input meme file, support wildcard")
	parser.add_argument("-k", "--knum", help="max number of individual files")


	args = parser.parse_args()
	memefile=args.memefile
	k=int(args.knum)

	#k=15

	motifs=open(memefile).read().strip().split('MOTIF')
	header = motifs [0]
	motifs=motifs[1:]
	binsize=len(motifs)/k+1

	count=1
	out=open(memefile+"."+str(count)+".meme",'w')
	for m in range(len(motifs)):
		if m!=0 and m%binsize==0:
			out.close()
			count+=1
			out=open(memefile+"."+str(count)+".meme",'w')
			out.write(header+'MOTIF'+motifs[m]+'\n')
		else:
			out.write(header+'MOTIF'+motifs[m]+'\n')
	out.close()
	
	return

if __name__=="__main__":
	main()


