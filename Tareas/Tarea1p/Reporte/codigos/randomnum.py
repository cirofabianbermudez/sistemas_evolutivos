# Autor: Ciro Fabian Bermudez Marquez
# 02.02.2021

# Librerias
import sys
import random

n = len(sys.argv)
if n != 3 :
	print( "Args valor inicial" )
	sys.exit(1)

inicio = int( sys.argv[1] )
fin  = int( sys.argv[2] )

# Para int
#print( random.randint( inicio, fin ) )
# Para float
print( random.uniform( inicio, fin) ) 
