#! /bin/bash
# Autor: Ciro Fabian Bermudez Marquez
# 02.02.2021

for (( i=1; i<=100; i+=1))
do
	randnum=$(python3 randomnum.py 0 7)
	#echo $randnum
	#echo $i
	python3 newton2.py $randnum
done > datosfloat.txt
