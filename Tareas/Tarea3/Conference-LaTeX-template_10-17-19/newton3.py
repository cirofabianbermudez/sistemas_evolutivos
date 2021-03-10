import math

def Evalua( _n, vpar ) :
	suma = 0
	for i in range(_n):
		suma += (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
		v = 0.1*suma
	return v
