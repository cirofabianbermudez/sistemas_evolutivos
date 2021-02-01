#
# El método de Newton
# Fraga
# 25.01.2021
# 27.01.2021
import sys
import numpy as np

# La función de Rosenbrock
# de dos dimensiones y un solo objetivo
def rosenbrock( x, y ) :
	return (1.0 - x)*(1.0 - x) + 100.0*(y - x*x)*(y - x*x)


# El valor inicial de a
n = len(sys.argv)
if n != 3 :
	print( "Args: x0 y0" )
	sys.exit(1)

x = float( sys.argv[1] ) 
y = float( sys.argv[2] ) 

# Inicializamos la memoria para la jacobiana
# y la hesiana
J = np.zeros( (2,1) )
H = np.zeros( (2,2) )
Hinv = np.zeros( (2,2) )

# 20 iteraciones máximas
i = 1
while i <= 20 :

	J[0,0] = 2.0*(x-1.0) - 400.0*x*(y - x*x) 
	J[1,0] = 200.0*y - 200.0*x*x

	H[0,0] = 2.0 - 400.0*y + 1200.0 * x * x 
	H[0,1] = -400.0*x 
	H[1,0] = H[0,1]
	H[1,1] = 200.0

	detH = H[0,0]*H[1,1] - H[1,0]*H[0,1]   	

	Hinv[0,0] = H[1,1]/detH
	Hinv[1,1] = H[0,0]/detH
	Hinv[0,1] = -H[0,1]/detH
	Hinv[1,0] = -H[1,0]/detH

	Delta = -Hinv @ J 

	x += Delta[0,0]
	y += Delta[1,0]

	print( i, x, y )

	p = np.transpose(Delta) @ Delta
	# print( p )
	p = np.sqrt( p )
	# print( p )
	if p < 1e-10 :
		break

	i += 1

print( "f(x)=", rosenbrock(x, y) )
