# Execute genetic algorithm 500 times
#
out=$1
rm -f $out
touch $out
for (( i=0; i<500; i=i+1 ))
do
	echo $i
	../lshade $i >> $out
done
# awk -f p.awk $out
