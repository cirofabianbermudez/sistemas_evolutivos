# encoding: utf8

# Un programa para ordenar las soluciones
# a un problema multiobjetivo según la
# dominancia de Pareto
#
# Fraga 1.10.2019

# Entrada:
# Leemos todas las soluciones: 
# valores de las funciones objetivo y cada línea del
# archivo de entrada

# Salida:
# El conjunto de soluciones no dominadas
#
# Necesitamos:
# el nombre del archivo,
# número de objetivos
# número de restricciones (?)
#
# Leemos el archivo una sola vez para calcular
# el número de soluciones
import sys
import numpy
import dominancia

n = len( sys.argv )
if n != 3 :
	print( "Args: nombre_archivo num_objetivos" )
	sys.exit( 1 )

nombre = sys.argv[1]
m = int( sys.argv[2] )

# Contamos el número de soluciones
try:
	arch = open( nombre, "r" )
except:
	print( "No se puede abrir el archivo", nombre )
	sys.exit( 2 )

n = 0
while 1 :
	linea = arch.readline( )

	if linea == "" :
		break

	if linea[0] == '#' :
		continue

	n += 1

arch.seek( 0 )

# Tenemos n soluciones
#
soluciones = [0]*n
P = numpy.zeros( (n,n), dtype=int )
V = numpy.zeros( (n,m) )
lineas = [""]*n

# Leo las soluciones
i = 0
while 1 :
	linea = arch.readline( )

	if linea == "" :
		break

	if linea[0] == '#' :
		continue

	d = linea.split( )

	j = 0
	while j < m :
		V[i][j] = float( d[j] ) 
		j += 1

	lineas[i] = linea	

	i += 1

arch.close( )

i=0
while i < n :
	j = i+1
	while j < n :
		d = dominancia.dominancia( m, V[i], V[j] )
		# print i, j, d
		if d == 1 :    # V[i] domina
			soluciones[j] = 1	
		elif d == -1 : # V[j] domina
			soluciones[i] = 1	
		j += 1
	i += 1

# Imprimo las soluciones no dominadas
i = 0
while i < n :

	if soluciones[i] == 0 :
		print( lineas[i], end=' ' )

	i += 1
