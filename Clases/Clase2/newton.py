#
# El método de Newton
# Fraga
# 25.01.2021
import math
import sys

# Se necesitan las funciones para
# f(x), la primera derivada df(x),
# y la segunda derivada ddf(x)
def f(x) :
	return x*x*x - math.cos(x)

def df(x) :
	return 3.0*x*x + math.sin(x)

# El valor inicial de a
n = len(sys.argv)
if n != 2 :
	print( "Args: valor_inicial" )
	sys.exit(1)

a = float( sys.argv[1] ) 

# 20 iteraciones máximas
i = 1
while i <= 20 :
	Deltax = -f(a)/df(a)

	a += Deltax

	print( i, a )

	if abs(Deltax) < 1e-10 :
		break

	i += 1

print( "f(x)=", f(a) )
