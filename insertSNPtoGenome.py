from sys import argv

"""
	snpbedgraph = argv[1]
	genomefile = argv[2]
	outfile = argv[3]
"""
#read the genome:
def loadrefgenomefile(filename):
    #reads the reference genome from a single fasta file
    #takes care of many chromosomes in one file, takes care of many lines per chromosome
    genome={}
    seqs=open(filename).read().strip().split(">")[1:]
    for s in seqs:
        tmp=s.split()
        chromename=tmp[0]
        print "loading chromosome... "+chromename
        genome[chromename]=''.join(tmp[1:])
    return genome

def main():
	snpbedgraph = argv[1]
	genomefile = argv[2]
	outfile = argv[3]

	print "READING GENOME"
	genome = loadrefgenomefile(genomefile)

	print "READING SNP BEDGRAPH FILE"
	lines = open(snpbedgraph).readlines()
	#lines = lines[1:]

	snpdict = {} #organize the snp into chrommosomes
	for i in range(len(lines)):
	    tmp = lines[i].split()
	    chrom = tmp[0]
	    try:
	        loc = int(tmp[1])
	    except:
	        print tmp
	        continue
	    oldbase = tmp[4]
	    newbase = tmp[5]
	    try:
	        snpdict[chrom][loc] = newbase
	    except KeyError:
	        snpdict[chrom] = {}
	        snpdict[chrom][loc] = newbase

	print "Number of SNPs loaded", len(lines)


	for chrom in snpdict.keys():
		chrom2 = ''
		print "converting",chrom,"to list"
		if chrom == "chr23":
			chrom2 = "chrX"
		elif chrom == "chr24":
			chrom2 = "chrY"
		else:
		    chrom2 = chrom
		seqlist = list(genome[chrom2])
		count = 0
		for loc in snpdict[chrom]:
			count +=1 
			if count%10000==0:
				print count
			seqlist[loc] = snpdict[chrom][loc]
		print "converting back to string"
		genome[chrom2]=''.join(seqlist)


	print "ERROR checking"
	errorcount = 0
	for line in lines:
	    loc = int(line.split()[1])
	    tmp = line.split()
	    chrom = tmp[0]
	    newchar = ''
	    try:
	        newchar = tmp[6]
	    except IndexError:
	        continue
	    if newchar != genome[chrom][loc]:
	        errorcount += 1
	print "Total insertions",len(lines)
	print "Number of errors",errorcount


	#output the mutated genome:
	target = open(outfile,'w')
	for chrom in genome:
	    print chrom
	    target.write(">"+chrom+'\n')
	    target.write(genome[chrom]+'\n')
	target.close()

	return

if __name__=="__main__":
	main()