import pandas as pd
from sys import argv
import os

"""
TO USE:
program geneexpressionfile mutationfile ucsc_geneloc_file tag(thecancertype) outputdir
"""


#Filter the mutation samples and epxpression sample:
#if sample in expression:
#        if sample is normal (larger than ) Tumor types range from 01 - 09, normal types from 10 - 19:
#            add this sample to final set of samples
#        else:
#            dont add this smaple to final set
#if sample in mutation data:
#    if sample in mutation and not in expression:
#        dont add this sample
#    else:
#        add this sample to final sample set
#

def get_final_sample_set(geneexpression_file,mutation_file):
#Filter the mutation samples and epxpression sample:
#if sample in expression:
#        if sample is normal (larger than 9) #Tumor types range from 01 - 09, normal types from 10 - 19:
#            add this sample to final set of samples
#        else:
#            dont add this smaple to final set
#if sample in mutation data:
#    if sample in mutation and not in expression:
#        dont add this sample
#    else:
#        add this sample to final sample set
    
    samples_with_expression = open(geneexpression_file).readline().strip().split('\t')[1:]
    for i in range(len(samples_with_expression)):
        samples_with_expression[i] = '-'.join(samples_with_expression[i].split('-')[:4])
        
    samples_with_mutation = {}
    for line in open(mutation_file):
        s = '-'.join(line.split('\t')[0].split('-')[:4])
        samples_with_mutation[s] = 0
    #print samples_with_mutation
    
    finalsampleset = {}
    for s1 in samples_with_expression:
        code = 0
        try:
            code = int (s1.split('-')[-1][:2])
        except:
            print "ERROR",s1
        if  code >9:
            finalsampleset[s1] = 1
        else:
            continue
    for s2 in samples_with_mutation:
        if s2 in samples_with_expression:
            finalsampleset[s2] = 1
   
    return finalsampleset.keys()

def istumor(sample):
    if int (sample.split('-')[-1][:2]) > 9:
        return False
    return True

def makecovariate(finalsampleset,outfile):
    out = open(outfile,'w')
    line = "id"
    for s in sorted(finalsampleset):
        line +='\t'+s
    out.write(line+'\n')
    line= "mutation"
    for s in sorted(finalsampleset):
        if istumor(s):
            line +='\t'+'1'
        else:
            line +='\t'+'0'
    out.write(line+'\n')
    out.close()
    
    return

def format_mutation_and_genotype(mutationinputfile,tag,snp_location_out,genotype_out,finalsampleset):   
    file = open(mutationinputfile).read().split('\n')
    print len(file)
    mutations = {}
    samples = {}
    for line in file:
        tmp = line.strip().split('\t')
        if len(tmp)==1:
            continue
        mut = tmp[1]+'_'+tmp[2]
        sam = '-'.join(tmp[0].split('-')[:4])
        if mut not in mutations:
            mutations[mut] = 1
        else:
            mutations[mut] += 1
        if sam not in samples:
            samples[sam] = {mut:1}
        else:
            samples[sam][mut] = 1
    print len(samples)
    
    #mutations["chrX_1"]=1
    translatedict = {}
    for i in range(1,24):
        c = 'chr'+str(i)
        translatedict[c] =c 
    #translatedict
    
    
    #create a mutationname dict as well:
    mutnames = {}

    #make file SNP_locations:
    target = open(snp_location_out,'w')
    target.write("snp\tchr\tpos")
    mutationlocs = []
    factor = 10**12
    for mut in mutations:
        tmp = mut.split('_')
        try:
            loc = int(tmp[0].replace('chr',''))*factor + int(tmp[1])
        except:
            if 'x' in tmp[0] or 'X' in tmp[0]:
                loc = 25*factor + int(tmp[1]) #chrx is chr25
            elif 'y' in tmp[0] or 'Y' in tmp[0]:
                loc = 26*factor + int(tmp[1]) #chrx is chr26
            elif 'm' in tmp[0] or 'M' in tmp[0]:
                loc = 27*factor + int(tmp[1]) #chrx is chr27
        mutationlocs += [loc]
    mutationlocs = sorted(mutationlocs)
    for i in range(len(mutationlocs)):
        loc = mutationlocs[i]
        chromname = "chr"+str(loc/factor)
        try:
            chromname = translatedict[chromname]
        except:
            if chromname == 'chr25':
                chromname = 'chrX'
            elif chromname == 'chr26':
                chromname = 'chrY'
            elif chromname == 'chr27':
                chromname = 'chrM'
            else:
                print "ERROR",chromname
                continue
        mutname = "snp_"+tag+"_"+str(i+1)
        mutnames[mutname] = chromname+'_'+str(loc%factor)
        line = mutname +'\t'+chromname+'\t'+str(loc%factor)

        #print line
        target.write('\n'+line)
    target.close()
    
    ### Printing the genotype file
    #samplenames = sorted(samples.keys())
    samplenames = sorted(finalsampleset)
    target = open(genotype_out,'w')
    line = "id"
    for sam in samplenames:
        line += '\t'+'-'.join(sam.split("-")[:4])
    target.write(line)
    for i in range(len(mutnames)):
        mutname = "snp_"+tag+"_"+str(i+1)
        vector = [0]*len(samplenames)
        mutlocname = mutnames[mutname]
        for i in range(len(samplenames)):
            sam = samplenames[i]
            if sam in samples:
                if mutlocname in samples[sam]:
                    vector[i] = 1
        line = mutname+'\t'+'\t'.join(map(str,vector))
        target.write('\n'+line)
        #print mutname
        #print vector
    target.close()
    
    
def format_geneloc_and_geneexpression(ucsc_loc_file,expressionfile,tag,genelocation_out,geneexpression_out,finalsampleset):
    
    # get the locations of the gene existing in the file. 
    locationfile = ucsc_loc_file
    genelocdict = {}
    #count = 0
    for line in open(locationfile):
        #count +=1 
        #if count == 10:
        #    break
        #print line
        tmp = line.split('\t')
        #print tmp[8]
        genelocdict[tmp[7]] = [tmp[1],tmp[3]]
        
        genes = {}
    output1 = open(genelocation_out,'w')
    output2 = open("geneexpression_out.tmp",'w')

    line = "id\t"+'\t'.join(open(expressionfile).readline().split('\t')[1:])
    output2.write(line)


    output1.write("geneid\tchr\ts1\ts2\n")
    #samples_in_expression:
    genes_seen = {}
    gene_nointlocationcount = 0
    for line in open(expressionfile):
        tmp = line.strip().split('\t')
        gene = tmp[0].split('|')[0]
        if gene in genelocdict and gene not in genes_seen:
            genes_seen[gene] = 1
            line1 = gene+'\t'+'\t'.join(genelocdict[gene])+'\t'+genelocdict[gene][1]
            output1.write(line1+'\n')
            line2 = gene+'\t'+'\t'.join(tmp[1:])
            output2.write(line2+'\n')
        else: 
            gene_nointlocationcount += 1
    print "genes not found in ucsc list",gene_nointlocationcount
    output1.close()
    output2.close()
    
    #filter the gene expression another time. 
    # get only samples from the final set
    data = pd.read_csv("geneexpression_out.tmp",sep = '\t',index_col=0)
    columnames = list(data)
    rownames = list(data.index)

    finaldata = {}
    for col in columnames:

        s = '-'.join(col.strip().split('-')[:4])
        #print col,s
        if s in finalsampleset:
            finaldata[s] = list(data[col])
        else:
            continue
    output3 = open(geneexpression_out,'w')
    line = 'id'
    for s in sorted(finalsampleset):
        line += '\t' + s
    #print line
    output3.write(line+'\n')
    numline = len(finaldata[finalsampleset[0]])
    for i in range(numline):
        line = rownames[i]
        #print line 
        for s in sorted(finalsampleset):
            #print finaldata[s][i]
            line += '\t' + str(finaldata[s][i])
        output3.write(line+'\n')
    output3.close()
    
    return




#INPUTS

geneexpression_file = argv[1]
#geneexpression_file = "/Users/vungo/Work/gdac.broadinstitute.org_CHOL.Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.Level_3.2016012800.0.0/CHOL.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.data.txt"

mutationfile = argv[2]
#mutationfile = "/Users/vungo/Work/gdac.broadinstitute.org_CHOL-TP.Mutation_CHASM.Level_4.2016012800.0.0/mutationslist.txt"

ucsc_loc_file = argv[3]
#ucsc_loc_file = "/Users/vungo/Google_Drive/UCSC_gene_loc_and_names.txt"

tag = argv[4]
#tag = "CHOL"

# directory containg all 5 requireed files
outdir = argv[5]

os.system("mkdir "+outdir)

#snp_locationoutut = argv[5]
snp_locationoutut = outdir+'/'+tag+".snp_locations.txt"

genotypeout = outdir+'/'+tag+".genotype.txt"

covariatefile = outdir+'/'+tag+".covariates.txt"

genelocation_out = outdir +'/'+tag+".genelocations.txt"

geneexpression_out = outdir +'/'+tag+".geneexpressions.txt"



#get the final sample set
finalsampleset = get_final_sample_set(geneexpression_file,mutationfile)

format_mutation_and_genotype(mutationfile,tag,snp_locationoutut,genotypeout,finalsampleset)

format_geneloc_and_geneexpression(ucsc_loc_file,geneexpression_file,tag,genelocation_out,geneexpression_out,finalsampleset)

makecovariate(finalsampleset,covariatefile)
    