# Método de newton
# Ciro Fabian Bermudez Marquez
# 01.02.2021

# Librerias
import math
import sys

# Funciones para el método

def f(x) :
	return x*x*x - math.cos(x) 

def df(x) :
	return 3.0*x*x + math.sin(x) 

n = len(sys.argv)
if n != 2 :
	print("Args: valor_inicial")
	sys.exit(1)
xr = float( sys.argv[1] )

# 20 iteraciones
print("i \txi \t\tea")	
i = 0
while i <= 20 :
	xrold = xr
	xr = xrold - f(xrold)/df(xrold)
	# temp =- f(xrold)/df(xrold) 
	i += 1
	error = 100.0*abs((xr - xrold)/xr)
	print("%2d \t%3.5f \t%3.5f" %(i,xr,error))	
	
	if abs(error) < 1e-10 :
		break	


print( "x = ", xr, "f(x) = ", f(xr) )

