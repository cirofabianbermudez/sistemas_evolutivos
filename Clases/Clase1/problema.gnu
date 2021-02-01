# un script para gnuplot
# 20.01.2021

# una función cuadrática

set xrange [-2:7]
set grid

f(x) = (x - 1.0)*(x - 5.0) - 10
# = x^2 - 6x + 5 - 10
# = x^2 - 6x - 10

df(x) = 2.0*x - 6

plot f(x), df(x)
pause -1


