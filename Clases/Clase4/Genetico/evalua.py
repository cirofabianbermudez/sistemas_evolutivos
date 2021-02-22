# coding: utf-8
import math

def Evalua( _n, vpar ) :
	suma = 0
	for i in range(_n):
		suma = suma +  (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
	
	v = 0.1*suma

	return v


# La función esférica:
def Evalua1( _n, vpar ) :
 	i=0
 	suma=0.0
 	while i<_n :
 		v = vpar[i]
 		suma += v*v
 		i += 1
 
 	return( suma )

# _n : es el número de variables
# vpar : el vector con los valores para cada variable
# def Evalua( _n, vpar ):
# 	x = vpar[0]
# 
# 	r = (x-10.0)*(x-10.0) + 10.0 + 2.0 * math.cos( 2.0*x )
# 
# 	return r
