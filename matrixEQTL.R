#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE);

#usages Rscript --vanilla matrixEQTL.R geneexpression snp_genotype snp_locs genelocs covariates cis_out trans_out

#df = read.table(args[1], header=TRUE)


require("MatrixEQTL")


geneExfile = args[1];

data = read.csv(geneExfile,sep='\t',row.names =1);
data.log = log(data+1) #adding 1 solves the log(0) problem

lognormedExpressionfile = paste(geneExfile,"lognorm",sep='.');
write.table(data.log, file = lognormedExpressionfile,quote=FALSE, sep ='\t');



# Linear model to use, modelANOVA, modelLINEAR, or modelLINEAR_CROSS
useModel = modelLINEAR; # modelANOVA, modelLINEAR, or modelLINEAR_CROSS

# Genotype file name
#SNP_file_name = paste(base.dir, "/data/SNP.txt", sep="");
#snps_location_file_name = paste(base.dir, "/data/snpsloc.txt", sep="");
SNP_file_name = args[2]#"~/Work/testGenotype.txt";
snps_location_file_name = args[3] #"~/Work/testSNP_locations.txt";

# Gene expression file name
#expression_file_name = paste(base.dir, "/data/GE.txt", sep="");
#gene_location_file_name = paste(base.dir, "/data/geneloc.txt", sep="");
expression_file_name = lognormedExpressionfile;
gene_location_file_name = args[4] #"~/Work/testGenelocations.txt";

# Covariates file name
# Set to character() for no covariates
#covariates_file_name = paste(base.dir, "/data/Covariates.txt", sep="");
covariates_file_name =  args[5] #"~/Work/testCovariate.txt";

table = read.csv(covariates_file_name,sep='\t')
L = unname(unlist(table))
if (0 %in% L) #check if any normal sample in it
    {
    covariates_file_name = covariates_file_name
    } 
else 
    {
    covariates_file_name = character()
    }



# Output file name
output_file_name_cis = args[6] #"~/Work/CHOL_eqtl_cis.tsv";
output_file_name_tra = args[7] #"~/Work/CHOL_eqtl_trans.tsv";

# Only associations significant at this level will be saved
pvOutputThreshold_cis = 2e-3;
pvOutputThreshold_tra = 1e-3;

# Error covariance matrix
# Set to numeric() for identity.
errorCovariance = numeric();
# errorCovariance = read.table("Sample_Data/errorCovariance.txt");

# Distance for local gene-SNP pairs
cisDist = 1e6;




#Load SNP data (Load genotype data)

snps = SlicedData$new();
snps$fileDelimiter = "\t";      # the TAB character
snps$fileOmitCharacters = "NA"; # denote missing values;
snps$fileSkipRows = 1;          # one row of column labels
snps$fileSkipColumns = 1;       # one column of row labels
snps$fileSliceSize = 2000;      # read file in slices of 2,000 rows
snps$LoadFile(SNP_file_name);


## Load gene expression data

gene = SlicedData$new();
gene$fileDelimiter = "\t";      # the TAB character
gene$fileOmitCharacters = "NA"; # denote missing values;
gene$fileSkipRows = 1;          # one row of column labels
gene$fileSkipColumns = 1;       # one column of row labels
gene$fileSliceSize = 2000;      # read file in slices of 2,000 rows
gene$LoadFile(expression_file_name);


## Load covariates

cvrt = SlicedData$new();
cvrt$fileDelimiter = "\t";      # the TAB character
cvrt$fileOmitCharacters = "NA"; # denote missing values;
cvrt$fileSkipRows = 1;          # one row of column labels
cvrt$fileSkipColumns = 1;       # one column of row labels
if(length(covariates_file_name)>0) {
cvrt$LoadFile(covariates_file_name);
}


snpspos = read.table(snps_location_file_name, header = TRUE, stringsAsFactors = FALSE);
genepos = read.table(gene_location_file_name, header = TRUE, stringsAsFactors = FALSE);


#Running analysis

me = Matrix_eQTL_main(
snps = snps, 
gene = gene, 
cvrt = cvrt,
output_file_name     = output_file_name_tra,
pvOutputThreshold     = pvOutputThreshold_tra,
useModel = useModel, 
errorCovariance = errorCovariance, 
verbose = TRUE, 
output_file_name.cis = output_file_name_cis,
pvOutputThreshold.cis = pvOutputThreshold_cis,
snpspos = snpspos, 
genepos = genepos,
cisDist = cisDist,
pvalue.hist = "qqplot",
min.pv.by.genesnp = FALSE,
noFDRsaveMemory = FALSE);


unlink(output_file_name_tra);
unlink(output_file_name_cis);


#print results 
write.table(me$cis$eqtls,file = output_file_name_cis,sep='\t',quote=FALSE)
write.table(me$trans$eqtls,file = output_file_name_tra,sep='\t',quote=FALSE)


cat('Analysis done in: ', me$time.in.sec, ' seconds', '\n');