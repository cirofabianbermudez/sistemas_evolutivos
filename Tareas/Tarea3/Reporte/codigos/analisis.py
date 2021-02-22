# Autor: Ciro Fabian Bermudez Marquez
# 02.02.2021

# Librerias
import math
import numpy as np
import collections

def df(x) :
	return 2.0*x - 7 + 1.5*math.pi*math.cos(1.5*math.pi*x) 


def ddf(x) :
	return 2.0 - 1.5*math.pi*1.5*math.pi*math.sin(1.5*math.pi*x)


data = np.genfromtxt( "datosfloat.txt" )
tam = len(data)  
xp = []
min_global = 3.6528874421621778 

#cont = 0	# Apariciones minimo global
num_fallas = 0	
num_neg = 0	# Apariciones de soluciones negativas
for i in range( tam ):
	is_zero =  df( data[i] ) 	
	if  is_zero  < 1e-4 :		# La solucion es correcta
		if data[i] < 0 :
			num_neg += 1
		else :
			#print( i ,data[i] )
			xp.append( data[i] )
		#if abs( data[i] - min_global ) <= 1e-4 :	# Contar minimo
		#	cont += 1
	else:
		num_fallas += 1


xp = np.array(xp)				 # Convertir a objeto de numpy
freq = collections.Counter(xp.round(12))

for key,value in freq.items() :
	if ddf( float(key) )  < 0 :
		s = "maximo"
	elif ddf( float(key) )  > 0 :
		s = "minimo"
	else :
		s = "ninguno"
	print(key,value,s)

freq["fallos"] = num_fallas
freq["<0"] = num_neg
print(freq)
print(num_fallas,num_neg)
