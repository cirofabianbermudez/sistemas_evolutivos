import numpy

def gray2dec3( g, indice, tamanio, w ) :
	numero = 0
	b = 0
	j = indice+tamanio-1
	if g[j] :
		b = 1
		numero = w[j]

	j=tamanio-2
	while j>=0 :
		b = g[indice+j] ^ b
		if b : 
			numero = numero + w[j]
		j = j-1

	return numero

w = numpy.zeros( 8, dtype=numpy.int32 )
w[0] =   1
w[1] =   2
w[2] =   4
w[3] =   8
w[4] =  16
w[5] =  32
w[6] =  64
w[7] = 128

numero = numpy.zeros( 5, dtype=numpy.int8 )

bin = (0,1)

for i in bin :
	numero[0] = i

	for j in bin :
		numero[1] = j
		
		for k in bin :
			numero[2] = k

			for l in bin :
				numero[3] = l

				for m in bin :
					numero[4] = m
					# print numero[0], numero[1], numero[2]
					v = gray2dec3( numero, 0, 5, w )
					print numero[4], numero[3], numero[2], numero[1], numero[0], v
