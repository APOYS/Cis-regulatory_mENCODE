from sys import argv
import os



def main():
	indir = argv[1] #containing a dir for of separate motifs in meme format
	fasta = argv[2]
	template = argv[3] # the template for the qsub file
	outdir = argv[4] #the output scanning file

	template = open(template).read()

	print template

	for file in os.listdir(indir):
		if "meme" in file and "scanned" not in file:
			meme = file
			output = file+".scanned"
			content = template.replace("MEME", indir +'/'+meme)
			content = content.replace("DIR", indir)
			content = content.replace("OUTPUT", meme)
			content = content.replace("FASTA", fasta)
			target = open(file+".qsub")
			target.write(content)
			target.close()



	return 

if __name__=="__main__":
	main()