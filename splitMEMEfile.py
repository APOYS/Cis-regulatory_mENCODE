"""
IN: MEMEfile, number of subfile k
OUT: k subfiles 
"""

from sys import argv

def main():
	memefile=argv[1]
	k=int(argv[2])

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


