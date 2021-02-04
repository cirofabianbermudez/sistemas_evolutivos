# Autor: Ciro Fabian Bermudez Marquez
# 01.02.2021

# Configuraciones de ventana
set terminal epslatex   
set output "filename.tex"
set grid
set title "$f(x) = (x-2)(x-3) + \sin(1.5 \pi x)$"
set xlabel "$x$"
set ylabel "$f(x)$"
f(x) = (x-2.0)*(x-5.0) + sin(1.5*pi*x)
# f(x) = 2.0*x -7.0 + 1.5*pi*cos(1.5*pi*x) 
plot [0:7] f(x)

pause -1
