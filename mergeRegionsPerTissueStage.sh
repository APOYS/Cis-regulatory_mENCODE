for tissue in {Cranio,Forebrain,Midbrain,Hindbrain,Neural,Heart,Liver,Limb,Lung,Kidney,Stomach,Intestine}; do
	for stage in {E11.5,E13.5,E14.5,E15.5,E16.5,P0}; do
		echo $tissue $stage
		cat TissueStageallpeaks/$tissue*$stage*.bed | sort -k1,1 -k2,2n > TissueStageallpeaks/$tissue.$stage.ALL.sorted.bed
		bedtools merge -i TissueStageallpeaks/$tissue.$stage.ALL.sorted.bed > TissueStageallpeaks/$tissue.$stage.ALL.merged.bed
	done
done
