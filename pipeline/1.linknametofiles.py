import os 
from sys import argv

"""Creating links to the bedfiles, name the links based on their information"""

#beddir=argv[1]
#bedmetadata=argv[2]
bedmetadata="/Users/vungo/Downloads/metadata.tsv"
sampleinfo='samples.csv'
#sampleinfo=argv[3]
#prefix=argv[4] #this is the prefix of the links, use absolute paths

s="ENCFF788SXX,H3K4me2,E14.5,Kidney,1,ExpAcc:ENCSR658TDS md5sum:6a2c2a715bd798fb728d4eccf8828bc1 URL:https://www.encodeproject.org/files/ENCFF788SXX/@@download/ENCFF788SXX.bam genomeversion:mm10,renlab"

def makenewname(seq):
	"""put the info in here, make a new name based on it
	example:
	IN: ENCFF788SXX,H3K4me2,E14.5,Kidney,1,ExpAcc:ENCSR658TDS md5sum:6a2c2a715bd798fb728d4eccf8828bc1 URL:https://www.encodeproject.org/files/ENCFF788SXX/@@download/ENCFF788SXX.bam genomevers
	OUT: [ENCSR658TDS , Kidney_E14.5_H3K4me2]
	"""
	tmp=seq.strip().split(" ")[0]
	exp=tmp.strip().split(':')[1]
	tmp2=tmp.split(',')
	name=tmp2[3]+"_"+tmp2[2]+"_"+tmp2[1]

	return exp,name
def loadsampleinfo(file):
	infodict={}
	lines=open(file).read().strip().split('\n')
	for l in lines:
		if "ID,Marker," not in l:
			exp,name=makenewname(l)
			if "tube" in name:
				name=name.replace('tube','Tube')
			if "facial" in name:
				name=name.replace("facial",'Facial')
			infodict[exp]=name
	return infodict

def loadmetadata(file):
	lines=open(file).read().strip().split('\n')
	acToExpdict={}
	for l in lines:
		tmp=l.strip().split('\t')
		acToExpdict[tmp[0]]=tmp[3]

	return acToExpdict

#print makenewname(s)
expInfodict=loadsampleinfo(sampleinfo)
actoexp=loadmetadata(bedmetadata)
#del actoexp['Experiment accession']

bedtoinfodict={}
for i in actoexp:
	if "ENC" in actoexp[i]:
		print i,actoexp[i],expInfodict[actoexp[i]]
		bedtoinfodict[i]=expInfodict[actoexp[i]]

for bf in bedtoinfodict:
	bedfile=prefix+'/'+bf+'.bed'
	link=bedtoinfodict[bf]
	os.system('ln -s '+bedfile+" "+link)
	





