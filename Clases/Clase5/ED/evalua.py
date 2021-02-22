import math

def Evalua( _n, vpar ) :
	suma = 0
	for i in range(_n):
		suma = suma +  (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
		v = 0.1*suma
	return v


# # coding: utf-8

# # La función esférica:
# def EvaluaEsferica( _n, vpar ) :
	# i=0
	# suma=0.0
	# while i<_n :
		# v = vpar[i]
		# suma += v*v
		# i += 1

	# return( suma )

# # Función Styblinski-Tank
# #
# # http://benchmarkfcns.xyz/benchmarkfcns/styblinskitankfcn.html
# #
# def Evalua( _n, vpar ) :
	# i=0
	# suma=0.0
	# while i<_n :
		# v = vpar[i]
		# v2 = v*v
		# suma += v2*v2 - 16.0*v2 + 5.0*v
		# i += 1

	# return( 0.5*suma )
