import sys
import numpy as np
import f
#
# The newton method to find the roots of a function
# Fraga 18.03.2020
# Guarda los datos de la simulación

n = len( sys.argv )
if n != 3 :
	print( "Args: inicial_value file_name" )
	sys.exit(1)

x = float( sys.argv[1] )
nombre = sys.argv[2]

try :
	arch = open( nombre, "w" )
except :
	print( "Can't open output file", name )
	sys.exit(1)


X = np.zeros( (1,3) )
j = 0
print( "0", x )
i = 0
while i < 20 :  # 20 maximum iterations
	funcion = f.df1(x)
	dfuncion = f.ddf1(x)
	X[0,0] = x
	X[0,1] = funcion 	
	X[0,2] = dfuncion
	X.tofile( arch )
	Deltaa = -funcion/dfuncion
	x += Deltaa

	print( i+1, x )

	if abs(Deltaa) < 1e-10 :
		break

	i += 1

arch.close( )
