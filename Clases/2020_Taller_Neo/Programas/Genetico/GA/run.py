# coding: utf-8
import ga

def PrintPopulation( D ):
	print( "Population:" )
	i=0
	while i<D._pop :
		print( D.Pop1[i], D.vfobj1[i] )
		i += 1

# An instance of GA
Data = ga.GA()

# Set GA parameters:
#    1 population size
#    2 number of generations
#    3 number of variables
#    4 crossover probability
#    5 mutation probability
# Data.SetParameters( 10, 5, 1, 0.7, 0.1  ) 
Data.SetParameters( 20, 30, 1, 0.7, 0.1  )

# Args: list with the size in bits for each variable
Data.SetSizes( [10] ) 

# Two lists to set the minimum and maximun values for each
# variable
Data.SetLimits( [0.0], [7.0] ) 

Data.Initialize( )
Data.EvaluatePopulation()
Data.SearchBestIndividual( )
Data.StoreData( "g1.bin" )
i=0;
while i<Data._gen :
	j=0
	while j<Data._pop :
		father1 = Data.Select()
		father2 = Data.Select()

		Data.Crossover( father1, father2, j )

		Data.Mutate( j )
		Data.Mutate( j+1 )

		Data.EvaluateChild( j )
		Data.EvaluateChild( j+1 )
		j += 2
	
	Data.ChangePopulations( )
	# Here elitism is applied:
	Data.SearchBestIndividual( )

	# print( "i:", i )
	# Data.PrintBestIndividual( )
	# PrintPopulation( Data )
	Data.SavePopulation( )

	i += 1

Data.PrintBestIndividual( )
Data.End( )

# print( "Final Population:" )
# PrintPopulation( Data )
