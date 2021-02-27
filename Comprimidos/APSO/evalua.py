import math

# La función esférica:
def EvaluaEsferica( _n, vpar ) :
	i=0
	suma=0.0
	while i<_n :
		v = vpar[i]
		suma += v*v
		i += 1

	return( suma )

# Función Styblinski-Tank
#
# http://benchmarkfcns.xyz/benchmarkfcns/styblinskitankfcn.html
#
def Evalua1( _n, vpar ) :
	i=0
	suma=0.0
	while i<_n :
		v = vpar[i]
		v2 = v*v
		suma += v2*v2 - 16.0*v2 + 5.0*v
		i += 1

	return( 0.5*suma )

def Evalua2( _n, vpar ) :
	x = vpar[0]
	y = (x - 2.0)*(x - 5.0) + math.sin(1.5*math.pi*x)
	return y

# Un problema con una restricción
# resulto por el método de penalización
def Evalua( _n, vpar ) :

	x = vpar[0]
	y = (x - 2.0)*(x - 5.0) + math.sin(1.5*math.pi*x)

	# La restricción:
	# y - 5.0 - 2.5*(x - 6) >= 0
	g = y - 5.0 - 2.5*(x - 6)

	# min( 0, g ) 
	if g < 0.0 :
		v = g
	else :
		v = 0.0

	return y + 20.0*v*v
