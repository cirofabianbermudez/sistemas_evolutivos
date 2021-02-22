# coding: utf-8
import ag

# Una instancia del AG
Datos = ag.AG()

# Pone los parámetros para el genético
# 1 tamaño de poblacion
# 2 número de generaciones
# 3 número de variables
# 4 probalidad de cruza
# 5 probalidad de mutacion
Datos.PoneParametros( 10, 20, 1, 0.8, 0.2  ) 

# Args: una lista con el tamaño en bits para cada variable
Datos.PoneTamanios( [8] ) 

#  Dos listas, para el mínimo y para el máximo para cada
# variable
Datos.PoneLimites( [0], [255] ) 

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
	print i,
	Datos.ImprimeMejor( )

	i += 1

Datos.ImprimeMejor( )
# print "Población final:"
# i=0
# while i<Datos._pop :
# 	print Datos.Pop1[i], Datos.vfobj1[i]
# 	i += 1
