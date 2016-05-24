"""
Input: 2 files
	- coverage bedfile
	- binned 500 merged peak file
	- outfile

Out: filtered coverage bedfile
"""
from sys import argv

def main():
	covfile=argv[1]
	peakfile=argv[2]
	outfile=argv[3]

	peaks={}
	for line in open(peakfile):
		tmp=line.split('\t')
		name=tmp[0]+'_'+tmp[1]
		peaks[name]=1

	out=open(outfile,'w')
	for line in open(covfile):
		tmp=line.split('\t')
		name=tmp[0]+"_"+tmp[1]
		if name in peaks:
			out.write(name+"\t"+tmp[3])
	out.close()

	return

if __name__=="__main__":
	main()