
f1(x) = x*x
f2(x) = x*log(x)

set xlabel "n"
set ylabel "Complejidad"
set xrange [0:1000]
set key left
plot f1(x) t "O(n^2)", f2(x) t "O(n log n )"
pause -1
