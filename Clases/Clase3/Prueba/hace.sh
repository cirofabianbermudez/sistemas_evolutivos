salida="sale.txt"
rm -f $salida
touch $salida
for(( i=0; i<100; i+=1 ))
do
	echo $i
	python algoritmo.py $i 20 >> $salida
done
