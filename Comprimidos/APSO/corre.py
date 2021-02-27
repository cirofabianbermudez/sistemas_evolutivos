# Accelerated Particle Swarm Optimization
# Fraga 10/02/2021
import apso

Datos = apso.APSO()

# Argumentos:
# Tamaño de poblacion
# Generaciones
# Número de variables
Datos.PoneParametros( 20, 60, 1 )
# Datos.PoneLimites( [0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0] )
Datos.PoneLimites( [0.0], [7.0] )

Datos.Inicializa( ) 
Datos.EvaluaPoblacion( ) 
Datos.EncuentraMejor( )

i=0
while i<Datos._gen :
	Datos.MueveParticulas( )      # Generar el nuevo individuo
	Datos.EvaluaPoblacion( ) 
	Datos.EncuentraMejor( )
	i += 1
	#if i%10 == 0 :
	#	Datos.ImprimeMejor()

Datos.ImprimeMejor()
