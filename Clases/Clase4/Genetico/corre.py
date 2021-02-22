# coding: utf-8
import ag

def imprime_poblacion( D ):
	print ( "Población:" )
	i=0
	while i<D._pop :
		print( D.Pop1[i], D.vfobj1[i] )
		i += 1

# Una instancia del AG
Datos = ag.AG()

# Pone los parámetros para el genético
# 1 tamaño de poblacion
# 2 número de generaciones
# 3 número de variables
# 4 probalidad de cruza
# 5 probalidad de mutacion
Datos.PoneParametros( 200, 150, 10, 0.7, 0.1  ) 

# Args: una lista con el tamaño en bits para cada variable
Datos.PoneTamanios( [10,10,10,10,10,10,10,10,10,10] ) 

#  Dos listas, para el mínimo y para el máximo para cada
# variable
Datos.PoneLimites( [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], [7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0] )

Datos.Inicializa( )
Datos.EvaluaPoblacion()
Datos.BuscaMejor( )
i=0;
while i<Datos._gen :
	j=0
	while j<Datos._pop :
		padre1 = Datos.Selecciona()
		padre2 = Datos.Selecciona()

		Datos.Cruza( padre1, padre2, j )

		Datos.Muta( j )
		Datos.Muta( j+1 )

		Datos.EvaluaHijo( j )
		Datos.EvaluaHijo( j+1 )
		j += 2
	
	Datos.CambiaPoblaciones( )
	# Se aplica el elitismo
	Datos.BuscaMejor( )
	# print "i:", i
	# Datos.ImprimeMejor( )

	i += 1

Datos.ImprimeMejor( )

# print "Población final:"
# imprime_poblacion( Datos )
