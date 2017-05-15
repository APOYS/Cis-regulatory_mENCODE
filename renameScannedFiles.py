from sys import argv
import os


def main():
	infile = argv[1]

	infilepath = "/".join(infile.split("/")[:-1])
	firstline = open(infile).readline()
	newname = infilepath + firstline.split()[3]+'.meme.scanned'
	command = "ln -s %s %s" %(infile,newname)
	os.system(command)
	return

if __name__=="__main__":
	main()