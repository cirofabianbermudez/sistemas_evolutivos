
set xrange [0:8]

f(x) = (x - 2.0)*(x - 5.0) + sin(1.5*pi*x)
# f(x) = x^2 - 7x + 10 + sin(1.5*pi*x)

df(x) = 2.0*x - 7 + 1.5*pi*cos(1.5*pi*x)

set grid
plot f(x), df(x)
pause -1
