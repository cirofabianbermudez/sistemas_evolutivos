# coding: utf-8
# Datos para un genético
import numpy
import random
import evalua

# pop => tamaño de la población
# gen => número de generaciones
# n   => número de variables
# pc  => probabilidad de cruza
# pm  => probabilidad de mutación
#
def PoneParametros1( self, pop, gen, n, pc, pm  ) :
	self._pop = pop
	if pop%2 :
		print( "ERROR: El tamaño de la población debe ser un número par" )

	self._gen = gen
	self._nv = n
	self._pc = pc
	self._pm = pm
	self.vmin = numpy.zeros( n ) 
	self.vmax = numpy.zeros( n ) 
	self.p2 = numpy.zeros( n ) 
	self.vtam = numpy.zeros( n, dtype=numpy.int ) 
	self.vindicesvar = numpy.zeros( n, dtype=numpy.int ) 
	self._posicionlista = 0

def Imprime1( self, i ) :
	print( self.Pop1[i], self.vfobj1[i] )

def PoneTamanios1( self, vtam ) :
	n = len( vtam )
	if n != self._nv :
		print( "Error: el vector de minimos debe tener {} valores".format( _nv ) )
		return -1
	i=0
	suma=0
	while i<n :
		self.vindicesvar[i] = suma
		self.vtam[i] = vtam[i]
		self.p2[i] = 2**vtam[i] - 1
		suma += vtam[i]
		i += 1

	self._tamanio = suma

	# La memoria para la población, Pop1; la nueva población de hijos, Pop2
	# y el valor de la función  objetivo de cada individuo
	self.Pop1 = numpy.zeros( (self._pop, suma), dtype=numpy.int8 ) 
	self.Pop2 = numpy.zeros( (self._pop, suma), dtype=numpy.int8 ) 
	self.vfobj1 = numpy.zeros( self._pop )
	self.vfobj2 = numpy.zeros( self._pop )
	self.vv = numpy.zeros( self._nv )
	self.vw = numpy.array( [1,2,4,8,16,32,64,128,256,512], dtype=numpy.int32 )
	self.vlista = numpy.zeros( self._pop, dtype=numpy.int32 )
	i = 0
	while i<self._pop :
		self.vlista[i] = i
		i += 1

	self.vmejor = numpy.zeros( self._tamanio, dtype=numpy.int8 )

	self._mejor = 0


def PoneLimites1( self, vmin, vmax ) :
	n = len( vmin )
	if n != self._nv :
		print( "Error: el vector de minimos debe tener {} valores".format( _nv ) )
		return -1

	n = len( vmax )
	if n != self._nv :
		print( "Error: el vector de maximos debe tener {} valores".format( _nv ) )
		return -2

	i=0
	while i<n :
		self.vmin[i] = vmin[i]
		self.vmax[i] = vmax[i]
		i += 1

def Inicializa1( self ) :
	i=0
	while i<self._pop :
		j=0
		while j<self._tamanio :
			k = random.random( )
			if k < 0.5 :
				v = 1
			else :
				v = 0

			self.Pop1[i][j] = v 
			j += 1
		i += 1

	i=0
	while i<self._tamanio :
		self.vmejor[i] = self.Pop1[0][i]
		i += 1



def Grey2Dec( g, indice, tamanio, w ) :
	numero = 0
	b = 0
	j = indice+tamanio-1
	if g[j] :
		b = 1
		numero = w[tamanio-1]

	j=tamanio-2
	while j>=0 :
		b = g[indice+j] ^ b
		if b : 
			numero = numero + w[j]
		j = j-1

	return numero


# Aquí se debería reparar el cromosoma:
# Se debería checar los límites de las variables
# y si no está entre los límites se generaría un valor
# aleatorio entre los límites y se cambia a código Grey
def EvaluaPoblacion1( self ) :
	i = 0
	while i<self._pop :
		j = 0
		while j < self._nv :
			b = Grey2Dec( self.Pop1[i], self.vindicesvar[j], self.vtam[j], self.vw )

			# self.vv[j] = v*20.0/255.0
			#  x  - min_x         b
			# -------------- = ---------
			#  max_x - min_x    2^p - 1

			self.vv[j] = b*(self.vmax[j] - self.vmin[j])/self.p2[j] + self.vmin[j] 
			j += 1

		self.vfobj1[i] = evalua.Evalua( self._nv, self.vv )
		i += 1

	# El mejor se inicializa al primer individio
	self._mejor = self.vfobj1[0]
	

def Selecciona1( self ) :
	if self._pop - self._posicionlista < 2 :
		random.shuffle( self.vlista )
		self._posicionlista = 0

	# Seleccionamos un individuo al azar
	ganador = self.vlista[ self._posicionlista ]
	otro    = self.vlista[ self._posicionlista + 1 ]

	#  AQUI se cambia si se MAXIMIZA o MINIMIZA
	# '<' MINIMIZA
	# '>' MAXIMIZA
	if self.vfobj1[ otro ] < self.vfobj1[ ganador] :
		ganador = otro
    
	self._posicionlista += 2;

	return( ganador )


# Parámetros: Tres índices a:
#            padre 1, padre 2, hijo 1, hijo 2 = hijo_1 + 1
# Los padres están en la matriz Pop1, los hijos en Pop2
def Cruza1( self, p1, p2, h1 ) :
	h2 = h1 + 1

	if random.random() <= self._pc :
		# k1 y k2 son dos puntos de cruza
		k1 = random.randint( 1, self._tamanio-1 )
		k2 = random.randint( 1, self._tamanio-1 )
		if k2<k1 : 
			tmp = k1
			k1 = k2
			k2 = tmp
		i=0
		while i<k1 :
			self.Pop2[h1][i] = self.Pop1[p1][i]
			self.Pop2[h2][i] = self.Pop1[p2][i]
			i += 1

		i=k1
		while i<k2 :
			self.Pop2[h1][i] = self.Pop1[p2][i]
			self.Pop2[h2][i] = self.Pop1[p1][i]
			i += 1

		i=k2
		while i<self._tamanio :
			self.Pop2[h1][i] = self.Pop1[p1][i]
			self.Pop2[h2][i] = self.Pop1[p2][i]
			i += 1
	else :  # Los hijos son iguales a los padres.
		i=0
		while i<self._tamanio :
			self.Pop2[h1][i] = self.Pop1[p1][i]
			self.Pop2[h2][i] = self.Pop1[p2][i]
			i += 1
	

# Muta solo sobre los hijos en la matriz Pop2
def Muta1( self, p ) :
	donde = random.randint( 0, self._tamanio-1 )

	if random.random() <= self._pm :
		if  self.Pop2[p][donde] == 1 :
			self.Pop2[p][donde] = 0 
		else :
			self.Pop2[p][donde] = 1 

def EvaluaHijo1( self, i ) :
	j = 0
	while j < self._nv :
		b = Grey2Dec( self.Pop2[i], self.vindicesvar[j], self.vtam[j], self.vw )
		self.vv[j] = b*(self.vmax[j] - self.vmin[j])/self.p2[j] + self.vmin[j] 
		j += 1

	self.vfobj2[i] = evalua.Evalua( self._nv, self.vv )

# Se está suponiendo que se minimiza
def BuscaMejor1( self ) :
	minimo = self.vfobj1[0]
	i = 1
	j = 0
	while i<self._pop :
		if self.vfobj1[i] <= minimo :
			j = i
			minimo = self.vfobj1[i]
		i += 1

	if minimo <= self._mejor :
		i=0
		while i<self._tamanio :
			self.vmejor[i] = self.Pop1[j][i]
			i += 1
		self._mejor = minimo

	else :
	 	i=0
	 	while i<self._tamanio :
	 		self.Pop1[j][i] = self.vmejor[i]
	 		i += 1
	 	self.vfobj1[j] = self._mejor


class AG:
	def __init__ ( self ) :
		self._pop=0  # tamaño de la población
		self._gen=0  # número generaciones
		self._nv=0   # número de variables
		self._pc=0   # probabilidad de combinación
		self._pm=0   # probabilidad de mutación

		self._tamanio=0 # tamanio del cromosoma
		self._fobjetivo=0 # indice al valor objetivo, = _tamanio

	PoneParametros = PoneParametros1
	PoneTamanios = PoneTamanios1
	PoneLimites = PoneLimites1
	Inicializa = Inicializa1
	EvaluaPoblacion = EvaluaPoblacion1
	Imprime = Imprime1
	Selecciona = Selecciona1
	Cruza  = Cruza1
	Muta = Muta1
	EvaluaHijo = EvaluaHijo1
	BuscaMejor = BuscaMejor1

	def ImprimeMejor( self ) :
	#	print( str(self.vmejor), end=' ' )

		j = 0
		while j < self._nv :
			b = Grey2Dec( self.vmejor, self.vindicesvar[j], self.vtam[j], self.vw )
			self.vv[j] = b*(self.vmax[j] - self.vmin[j])/self.p2[j] + self.vmin[j] 
	#		print( b, end=' ' )
			j += 1
		print( self._mejor )

	def CambiaPoblaciones( self ) :
		tmp = self.Pop1
		self.Pop1 = self.Pop2
		self.Pop2 = tmp
		i=0
		while i<self._pop :
			self.vfobj1[i] = self.vfobj2[i]
			i += 1
