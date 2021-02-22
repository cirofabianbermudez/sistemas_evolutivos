# coding: utf-8
#
# Here is defined the objective function
#
import math

# _n :  it is the number of variables 
# vpar : it is the vector with the values for each variable
#
def Evaluate( _n, vpar ) :
	x = vpar[0]
	v = (x-2)*(x-5) + math.sin( 1.5*math.pi*x )
	return v

# The same problema as before bur now with a constraint:
def Evaluate1( _n, vpar ) :

	x = vpar[0]
	y = (x-2.0)*(x-5.0) + math.sin(1.5*math.pi*x)

	g = y - 5.0 - 2.5*(x - 6.0)

	# The constraint is introduced according the penalization method :
	# 
	c = g
	if g > 0 :
		c = 0.0
	return( y + 20.0*c*c )



# La función esférica:
def Evaluate2( _n, vpar ) :
 	i=0
 	suma=0.0
 	while i<_n :
 		v = vpar[i]
 		suma += v*v
 		i += 1
 
 	return( suma )

# def Evalua( _n, vpar ):
# 	x = vpar[0]
# 
# 	r = (x-10.0)*(x-10.0) + 10.0 + 2.0 * math.cos( 2.0*x )
# 
# 	return r
