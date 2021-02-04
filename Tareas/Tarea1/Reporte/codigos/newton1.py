# El método de Newton
# Ciro Fabian Bermudez Marquez
# 02.02.2021
# Librerias
import math
import sys

# Funciones para el método
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
print("i \txi \t\tea")	
while i <= 20 :
	Deltax = -f(a)/df(a)
	a += Deltax
	print("%1d \t%3.5f \t%3.5f" %(i,a,Deltax))	

	if abs(Deltax) < 1e-10 :
		break

	i += 1

print( "x = ", a ,"f(x) = ", f(a) )
