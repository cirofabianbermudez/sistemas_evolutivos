import sys

n = len( sys.argv )
if n != 3 :
	print( "Args: a b" )
	sys.exit(1)

a = float( sys.argv[1] )
b = float( sys.argv[2] )

s = a + b
print( s )
