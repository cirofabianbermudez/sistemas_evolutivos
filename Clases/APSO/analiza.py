# coding: utf-8
import sys
import math

n = len( sys.argv )
if n != 2:
	print "Args: nombre_archivo"
	sys.exit(1)

nombre = sys.argv[1]

try:
	arch = open( nombre, "r" )
except:
	print "Error abriendo el archivo"
	sys.exit(2)

suma = 0
suma2 = 0
n=0
while 1 : 
	linea = arch.readline( )

	if linea == "" :
		break

	# proceso el archivo
	datos = linea.split( )
	if len(datos) == 5 :
		n += 1
		v = float(datos[4])
		suma += v
		suma2 += v*v

suma /= n
var = suma2/n - suma*suma

print n, suma, math.sqrt(var)
arch.close()
