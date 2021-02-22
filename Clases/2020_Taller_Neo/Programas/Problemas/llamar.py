import funcion
import sys

n = len( sys.argv )
if n != 2 :
	print( "Args: número" )
	sys.exit(1)

x = float( sys.argv[1] )

print( x, funcion.f(x) )
