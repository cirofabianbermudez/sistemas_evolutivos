import sys
import random

n = len( sys.argv )
if n != 3 :
	print( "Args: media d.e." )
	sys.exit(1)

media = float( sys.argv[1] )
desve = float( sys.argv[2] )

n = 100
i = 0
while i < n :
	x = random.gauss( media, desve )	
	print( x )
	i += 1
