# coding: utf-8
import numpy
import random
import evaluate

# Data for a genetic algorithm
# pop => population size
# gen => number of generations
# n   => numner of variables
# pc  => crossover probability
# pm  => mutation probability
#
def SetParameters1( self, pop, gen, n, pc, pm  ) :
	self._pop = pop
	if pop%2 :
		print( "ERROR: Population size must be an even number" )

	self._gen = gen
	self._nv = n
	self._pc = pc
	self._pm = pm
	self.vmin = numpy.zeros( n ) 
	self.vmax = numpy.zeros( n ) 
	self.vtam = numpy.zeros( n, dtype=numpy.int ) 
	self.delta = numpy.zeros( n )
	self.vindicesvar = numpy.zeros( n, dtype=numpy.int ) 
	self._listposition = 0

def Print1( self, i ) :
	print( self.Pop1[i], self.vfobj1[i] )

def SetSizes1( self, vtam ) :
	n = len( vtam )
	if n != self._nv :
		print( "Error: bits vector per variable must have {} values".format( _nv ) )
		return -1
	i=0
	suma=0
	while i<n :
		self.vindicesvar[i] = suma
		self.vtam[i] = vtam[i]
		suma += vtam[i]
		i += 1

	self._size = suma

	# La memoria para la población, Pop1; la nueva población de hijos, Pop2
	# y el valor de la función  objetivo de cada individuo
	self.Pop1 = numpy.zeros( (self._pop, suma), dtype=numpy.int8 ) 
	self.Pop2 = numpy.zeros( (self._pop, suma), dtype=numpy.int8 ) 
	self.vfobj1 = numpy.zeros( self._pop )
	self.vfobj2 = numpy.zeros( self._pop )
	self.vv = numpy.zeros( self._nv )
	self.vw = numpy.array( [1,2,4,8,16,32,64,128,256,512,1024], dtype=numpy.int32 )
	self.vlista = numpy.zeros( self._pop, dtype=numpy.int32 )
	i = 0
	while i<self._pop :
		self.vlista[i] = i
		i += 1

	self.vbest = numpy.zeros( self._size, dtype=numpy.int8 )

	self._best = 0


def SetLimits1( self, vmin, vmax ) :
	n = len( vmin )
	if n != self._nv :
		print( "Error: minima vector must have {} values".format( _nv ) )
		return -1

	n = len( vmax )
	if n != self._nv :
		print( "Error: maxima vector must have {} values".format( _nv ) )
		return -2

	i=0
	while i<n :
		self.vmin[i] = vmin[i]
		self.vmax[i] = vmax[i]
		self.delta[i] = (vmax[i] - vmin[i])/(self.vw[ self.vtam[i] ] - 1.0 )

		i += 1

def Initialize1( self ) :
	i=0
	while i<self._pop :
		j=0
		while j<self._size :
			k = random.random( )
			if k < 0.5 :
				v = 1
			else :
				v = 0

			self.Pop1[i][j] = v 
			j += 1
		i += 1

	i=0
	while i<self._size :
		self.vbest[i] = self.Pop1[0][i]
		i += 1



def Grey2Dec( g, indice, tamanio, w ) :
	number = 0
	b = 0
	j = indice+tamanio-1
	if g[j] :
		b = 1
		number = w[tamanio-1]

	j=tamanio-2
	while j>=0 :
		b = g[indice+j] ^ b
		if b : 
			number = number + w[j]
		j = j-1

	return number


# Here is where the chromosome should be repaired:
# Bound limits for each variable should be checked,
# and if that value is outside those limits a new
# random value is generated between the limits
# and then the variable is changed to Grey code.
def EvaluatePopulation1( self ) :
	i = 0
	while i<self._pop :
		j = 0
		while j < self._nv :
			v = Grey2Dec( self.Pop1[i], self.vindicesvar[j], self.vtam[j], self.vw )

			self.vv[j] = self.delta[j]*v + self.vmin[j]
			j += 1

		self.vfobj1[i] = evaluate.Evaluate( self._nv, self.vv )
		i += 1

	# The best individual is initialized as the first individual
	self._best = self.vfobj1[0]
	

def Select1( self ) :
	if self._pop - self._listposition < 2 :
		random.shuffle( self.vlista )
		self._listposition = 0

	# One individual is selected randomly 
	winner = self.vlista[ self._listposition ]
	otro    = self.vlista[ self._listposition + 1 ]

	#  HERE is change is the problem is MAXIMIZE ir MINIMIZE
	# '<' MINIMIZE
	# '>' MAXIMIZE
	if self.vfobj1[ otro ] < self.vfobj1[ winner ] :
		winner = otro
    
	self._listposition += 2;

	return( winner )


# Parameter: Three indexes to:
#            father 1, father 2, child 1, child 2 = child_1 + 1
# Fathers are in Pop1 matrix, children are in Pop2
def Crossover1( self, p1, p2, h1 ) :
	h2 = h1 + 1

	if random.random() <= self._pc :
		# k1 and k2 are two crossover points
		k1 = random.randint( 1, self._size-1 )
		k2 = random.randint( 1, self._size-1 )
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
		while i<self._size :
			self.Pop2[h1][i] = self.Pop1[p1][i]
			self.Pop2[h2][i] = self.Pop1[p2][i]
			i += 1
	else :  # Children are igual to parents
		i=0
		while i<self._size :
			self.Pop2[h1][i] = self.Pop1[p1][i]
			self.Pop2[h2][i] = self.Pop1[p2][i]
			i += 1
	

# Mutate is applied only on children in Pop2 matrix
def Mutate1( self, p ) :
	donde = random.randint( 0, self._size-1 )

	if random.random() <= self._pm :
		if  self.Pop2[p][donde] == 1 :
			self.Pop2[p][donde] = 0 
		else :
			self.Pop2[p][donde] = 1 

def EvaluateChild1( self, i ) :
	j = 0
	while j < self._nv :
		v = Grey2Dec( self.Pop2[i], self.vindicesvar[j], self.vtam[j], self.vw )
		self.vv[j] = self.delta[j] * v + self.vmin[j]
		j += 1

	self.vfobj2[i] = evaluate.Evaluate( self._nv, self.vv )

# It is suppose a minimization problem:
def SearchBestIndividual1( self ) :
	minimum = self.vfobj1[0]
	j = 0
	i = 1
	while i<self._pop :
		if self.vfobj1[i] <= minimum :
			j = i
			minimum = self.vfobj1[i]
		i += 1

	if minimum <= self._best :
		i=0
		while i<self._size :
			self.vbest[i] = self.Pop1[j][i]
			i += 1
		self._best = minimum

	else :
		i=0
		while i<self._size :
			self.Pop1[j][i] = self.vbest[i]
			i += 1
		self.vfobj1[j] = self._best


class GA:
	def __init__ ( self ) :
		self._pop=0  # population size
		self._gen=0  # number of generations
		self._nv=0   # number of variables
		self._pc=0   # crossover probability
		self._pm=0   # mutation probability

		self._size=0 # chromosome size

	SetParameters = SetParameters1
	SetSizes = SetSizes1
	SetLimits = SetLimits1
	Initialize = Initialize1
	EvaluatePopulation = EvaluatePopulation1
	Print = Print1
	Select = Select1
	Crossover  = Crossover1
	Mutate = Mutate1
	EvaluateChild = EvaluateChild1
	SearchBestIndividual = SearchBestIndividual1

	def PrintBestIndividual( self ) :
		print( self.vbest, end=' ' )

		j = 0
		while j < self._nv :
			v = Grey2Dec( self.vbest, self.vindicesvar[j], self.vtam[j], self.vw )
			v = self.delta[j] * v + self.vmin[j]
			print( v, end=' ' )
			j += 1
		print( self._best )

	def ChangePopulations( self ) :
		tmp = self.Pop1
		self.Pop1 = self.Pop2
		self.Pop2 = tmp
		i=0
		while i<self._pop :
			self.vfobj1[i] = self.vfobj2[i]
			i += 1

	def StoreData( self, name ) :
		if name != "" :
			self.debug = 1

		try :
			self.fp = open( name, "w" )
		except :
			print( "Can't open output file", name )
			self.debug = 0
			
	def End( self ) :
		self.fp.close( )	

	def SavePopulation( self ) :

		if self.debug == 0 :
			return

		# 
		# print( self.Pop1[i], self.vfobj1[i] )
		#
		i = 0
		while i<self._pop :
			j = 0
			while j < self._nv :
				v = Grey2Dec( self.Pop1[i], self.vindicesvar[j], self.vtam[j], self.vw )

				self.vv[j] = self.delta[j]*v + self.vmin[j]
				j += 1
			self.vv.tofile( self.fp ) 
			self.vfobj1[i].tofile( self.fp )
			i += 1
