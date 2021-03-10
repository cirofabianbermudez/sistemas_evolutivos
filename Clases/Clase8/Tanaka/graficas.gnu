set term pdf
set output "frente.pdf"
set xlabel "f1"
set ylabel "f2"
plot 'best_pop.out' t "Frente de Pareto" w p

set output "conjunto.pdf"
set xlabel "x"
set ylabel "Número de solución"
plot 'best_pop.out' u 3:($0) t "Conjunto de Pareto"  w p
