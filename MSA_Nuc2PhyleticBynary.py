"""
IN: MSA fasta format
OUT: MSA fasta but in bynary
"""

from sys import argv

infile = argv[1]
outfile = argv[2]


out = open(outfile,'w')
for line in open(infile):
	if line[0] == ">":
		#no altering
		out.write(line)
	else:
		line = line.strip()
		newline = ""
		for char in line:
			if char == "-":
				newline += "0"
			else:
				newline += "1"
		out.write(newline+'\n')
out.close()