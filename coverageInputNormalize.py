"""
INPUT: A input bedfile f
OUTPUT: normalized coverage files based on the input bedfile
"""

import os
from sys import argv

def main():
	inputbed=argv[1]

	prefix=inputbed.strip().split("Input")[0]+"H3K"
	print "Working on",prefix,'...'
	command="""for file in Cranio-facial_E11.5_H3K*.coverage; 
	do echo $file;input=Cranio-facial_E11.5_Input_Rep0_ENCFF851KTA_ENCFF265KAG.bed.500bin.coverage; 
	paste $file $input |awk 'function abs(value){return (value<0?0:value);};{ printf("%s\t%d\t%d\t%s\n", $1, $2, $3,abs($4-$11)); }' > $file.normalized;
	done"""
	print command
	os.system(command)

	return


if __name__=="__main__":
	main()