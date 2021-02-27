import math


def f(x):
	return (x-2.0)*(x-5.0) + math.sin(1.5 * math.pi * x)

def Evalua( _n, vpar ) :
	suma = 0
	for i in range(_n):
		suma = suma +  (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
	
	v = 0.1*suma

	return v

t = 3.65288744 
print(f(t))
