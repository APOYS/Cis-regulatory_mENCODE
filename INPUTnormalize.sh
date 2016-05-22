#!/bin/bash

input=INSERT_INPUT
for file in INSERTHERE; do
	paste $file $input |awk 'function abs(value){return (value<0?0:value);};{ printf("%s\t%d\t%d\t%s\n", $1, $2, $3,abs($4-$11)); }' > ${file/bed/normalized.bed};

	done
