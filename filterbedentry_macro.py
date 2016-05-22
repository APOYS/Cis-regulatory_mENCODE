from sys import argv
import os
def main():
	covfile=argv[1]
	basecovfile=covfile.split("/")[-1]
	tisuestage=basecovfile.split('_')[:2]
	mark=basecovfile.split('_')[2]
	outfile='_'.join(tisuestage+[mark])+".bin500.filtered.coverage"
	if "Cran" in tisuestage[0]:
		tisuestage[0]="Cranio"
	if "Neural" in tisuestage[0]:
		tisuestage[0]="Neural"

	regionfile='_'.join(tisuestage)+".sorted.merged.bin500"
	pathtoregion='/home/vungo/MouseENCODE_project/WorkingDCCdata/DCC_regions_bin500/X.mergedregions/'
	cmd="python ~/MouseENCODE_project/mENCODE_scripts/filterbedentry.py "+covfile+" "+pathtoregion+regionfile+" "+outfile
	#print cmd
	os.system(cmd)
	return

if __name__=="__main__":
	main()