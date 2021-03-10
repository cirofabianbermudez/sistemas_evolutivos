# Autor: Ciro Fabian Bermudez Marquez
# 01.02.2021

# Configuraciones de la ventana
# set terminal latex
# set output "test.tex"
set grid	# agregar la cuadricula
set title "Funcion"
set xrange [0:1]
set yrange [-1:1]
set xlabel "x"
set ylabel "f(x)"
# set label "hola" at 15,15

f(x) = exp(-x) - x 

plot f(x)
# with point
# with impulses
# with boxes
# para ver algunas configuraciones correr el comando test

pause -1
