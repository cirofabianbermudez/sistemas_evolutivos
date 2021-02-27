# coding: utf-8
import numpy
import random
import evalua

def Inicializa1( self ) :
	i = 0
	while i<self._pop :
		j = 0
		while j<self._nv :
			k = random.random( )
			v = self.Limites[0][j] + k * self.vamplitud[j]
			self.Pop[i][j] = v
			j += 1
		i += 1

def PoneParametros1( self, pop, gen, nv ) :
	self._pop = pop
	self._gen = gen
	self._nv  = nv
	self.Pop = numpy.zeros( (pop, nv+1) )
	self.mejor = numpy.zeros( nv+1 )
	#% Setting the parameters: alpha, beta
	#% Random amplitude of roaming particles gamma=[0,1]
	#% alpha=gamma^t=0.98^t;
	self.beta = 0.5
	self.alpha = 1.0
	self.gamma=(10**(-20)/self.alpha)**(1.0/gen);

def PoneLimites1( self, vmin, vmax ) :
	n = len( vmin )
	if n != self._nv :
		print( "ERROR: el vector de minimos es diferente que el número de variables" )

	n = len( vmax )
	if n != self._nv :
		print( "ERROR: el vector de maximos es diferente que el número de variables" )

	self.Limites = numpy.zeros( (2, self._nv) )
	self.vamplitud = numpy.zeros( self._nv )
	i = 0
	while i < self._nv :
		self.Limites[0][i] = vmin[i]
		self.Limites[1][i] = vmax[i]
		self.vamplitud[i] = vmax[i] - vmin[i]
		i += 1

def EvaluaPoblacion1( self ) :
	i = 0
	while i<self._pop :
		v = evalua.Evalua( self._nv, self.Pop[i] )
		self.Pop[i][self._nv] = v
		i += 1 

def MueveParticulas1( self ) :
	i = 0
	while i < self._pop :
		j = 0
		while j < self._nv :
			r = self.alpha*random.random()
			self.Pop[i][j] = self.Pop[i][j]*(1.0-self.beta) + self.mejor[j]*self.beta + r


			# checar los límites
			if self.Pop[i][j] < self.Limites[0][j] :
				self.Pop[i][j] = self.Limites[0][j]
	
			if self.Pop[i][j] > self.Limites[1][j] :
				self.Pop[i][j] = self.Limites[1][j]

			j += 1

		i += 1
	

class APSO:
	def __init__( self ) :
		self._pop = 0   # Tamaño de la población
		self._gen = 1   # Número de generaciones
		self._nv = 0    # Número de variables

	PoneParametros = PoneParametros1 
	PoneLimites = PoneLimites1 
	Inicializa =  Inicializa1
	EvaluaPoblacion = EvaluaPoblacion1
	MueveParticulas = MueveParticulas1

	def EncuentraMejor( self ) :
		v = self._nv
		miminimo = self.Pop[0][v]
		k = 0
		i = 1
		while i < self._pop :
			if self.Pop[i][v] < miminimo :
				miminimo = self.Pop[i][v]	
				k = i
			i += 1

		i = 0
		while i <= v :
			self.mejor[i] = self.Pop[k][i]
			i += 1

		self.alpha *= self.gamma

	def ImprimeMejor( self ) :
		v = self._nv

		i = 0
		while i <= v :
		#	print( self.mejor[i], end=' ' )
			i += 1
		print( self.mejor[10])
