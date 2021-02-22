import sys
import f
#
# The newton method to find the roots of a function
# Fraga 18.03.2020

n = len( sys.argv )
if n != 2 :
	print( "Args: inicial_value" )
	sys.exit(1)

x = float( sys.argv[1] )

i = 1
while i < 20 :  # 20 maximum iterations
	Deltaa = -f.df1(x)/f.ddf1(x)
	x += Deltaa

	print( i, x )

	if abs(Deltaa) < 1e-10 :
		break

	i += 1
