# coding: utf-8
# Fraga 12/06/2015
import ed

Datos = ed.ED()

# Argumentos:
# Tamaño de poblacion
# Generaciones
# Número de variables
# Constante de diferencias
# Constante de recombinacion
Datos.PoneParametros( 100, 70, 10, 0.2, 0.4 )
# Datos.PoneLimites( [0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0] )
Datos.PoneLimites( [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0] )

Datos.Inicializa( ) 
Datos.EvaluaPoblacion( ) 

i=0
while i<Datos._gen :
	j=0
	while j<Datos._pop :
		Datos.GeneraNuevo( j )      # Generar el nuevo individuo

		Datos.EvaluaNuevo( )  # Evaluarlo

		# Compararlo con el padre y si es mejor se sustituye
		Datos.ComparaNuevo( j )
		j += 1
	i += 1

Datos.ImprimeMejor()
