"""
INPUT: A input bedfile f
OUTPUT: normalized coverage files based on the input bedfile
"""

import os
from sys import argv

def main():
	#inputbed=argv[1]
	inputbed="Midbrain_E12.5_Input_Rep0_ENCFF595MDP_ENCFF233LRZ.bed.500bin.coverage"

	prefix=inputbed.strip().split("Input")[0]+"H3K"
	print "Working on",prefix,'...'
	command="""for file in """+prefix+"""*.coverage; 
	do echo $file;input="""+inputbed+"""; 
	paste $file $input |awk 'function abs(value){return (value<0?0:value);};{ printf("%s\\t%d\\t%d\\t%s\\n", $1, $2, $3,abs($4-$11)); }' > $file.normalized;
	done"""
	print command
	os.system(command)


	return


if __name__=="__main__":
	main()