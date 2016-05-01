#!/bin/bash


for dir in /data1/mEncode/Pipeline/DataLinks/Merged/bed/Group_By_Tissue_Stage/Heart*; 
do for bedfile in $dir/*;
	do tagdir=${bedfile##*/}.Tagnormalized; echo $tagdir;
	makeTagDirectory $tagdir -genome mm10 -normGC default -fragLength 290 $bedfile;
	done;
done
