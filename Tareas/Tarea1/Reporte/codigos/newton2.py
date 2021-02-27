# El metodo de Newton2
# Ciro Fabian Bermudez Marquez
# 02.02.2021
# Librerias
import math
import sys

# Funciones para el metodo
def df(x) :
	return 2.0*x - 7 + 1.5*math.pi*math.cos(1.5*math.pi*x) 

def ddf(x) :
	return 2.0 - 1.5*math.pi*1.5*math.pi*math.sin(1.5*math.pi*x)

# El valor inicial de a
n = len(sys.argv)
if n != 2 :
	print( "Args: valor_inicial" )
	sys.exit(1)

a = float( sys.argv[1] ) 

# 50 iteraciones maximas
i = 1
#print("i \txi \t\tea")	
while i <= 20 :
	Deltax = -df(a)/ddf(a)
	a += Deltax
	#print("%1d \t%3.5f \t%3.5f" %(i,a,Deltax))	

	if abs(Deltax) < 1e-10 :
		break

	i += 1

#print( "x = ", a ,"df(x) = ", df(a) )
# Solucion
print(a)
