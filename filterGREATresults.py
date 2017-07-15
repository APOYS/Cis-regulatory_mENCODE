from sys import argv
import os

infile = argv[1]
searchterm = argv[2]
#outfile = argv[3]

cmd = "grep %s %s|grep Biological > tmp.file" %(searchterm, infile)

#|cut -f1,3,5,7,14,16,24

os.system(cmd)
#read the results
binorm = 0.05
hyper = 0.05
for line in open("tmp.file"):
	tmp = line.strip().split('\t')
	#print tmp
	if float(tmp[6]) < binorm and float(tmp[15]) < hyper and float(tmp[7])>2 and float(tmp[18])>1:
		L = '\t'.join([tmp[0],tmp[2],tmp[4],tmp[6],tmp[13],tmp[15],tmp[23]])
		print L


