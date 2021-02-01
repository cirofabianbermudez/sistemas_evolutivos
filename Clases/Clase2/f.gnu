set xrange [-2:6]
set yrange [-10:10]
f(x) = (x-1.0)*(x-2.0)*(x-4.0)

f1(x) = 1 - x
f2(x) = 2.0*x*x - 13.0*x + 19.0
#
# f3(x)= x^3 - 7x^2 + 14x - 8
# f3(x) = x*(x*x - 7*x + 14.0) - 8.0
f3(x) = x*(x*(x - 7.0) + 14.0) - 8.0

plot f(x), f1(x), f2(x), f3(x)
pause -1
