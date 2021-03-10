# Python program to input info from command line

import sys
import math

n = len(sys.argv)
if n != 2 :
	print("Args: valor_inicial")
	sys.exit(1) 				# 0 significa without errors y 1 error

# El valor de la condicion inicial
xi = float( sys.argv[1] )

i = 1
while i <= 20 :
	xin = xi - f(xi)/df(xi)

print( "f(x) =", f(a) )
