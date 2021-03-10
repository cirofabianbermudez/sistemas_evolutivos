#set term pdf
#set output "frente.pdf"

reset

set terminal cairolatex standalone pdf size 16cm, 10.5cm dashed transparent \
monochrome header '\newcommand{\hl}[1]{\setlength{\fboxsep}{0.75pt}\colorbox{white}{#1}}'
set output 'generate.tex'

unset key
set grid xtics ytics ls 3 lw 1 lc rgb 'gray'


set xlabel '$f_{1}$'
set ylabel '$f_{2}$'
plot 'best_pop.out' u 1:2 t "Frente de Pareto" w p lc -1

#set output "conjunto.pdf"
#set xlabel "x"
#set ylabel "Número de solución"
#plot 'best_pop.out' u 3:($0) t "Conjunto de Pareto"  w p 
