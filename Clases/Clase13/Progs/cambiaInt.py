import sys
# of objectives = 2, # of constraints = 16, # of real_var = 5, # of bits of bin_var = 0, constr_violation, rank, crowding_distance
# -4.617922e+01	-3.747991e+04	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	1.000000e+00	9.879703e+01	5.521001e+01	6.184620e+01	9.923777e+01	2.407822e+00	0.000000e+00	1	1.000000e+14

objs = 2
constr = 16
varis  = 5

m = objs + constr + varis

n = len( sys.argv )
if n != 2 :
	print( "Args: archivo" )
	sys.exit(1)

try:
	arch = open( sys.argv[1], 'r' )
except:
	print("No puedo abrir el archivo", sys.argv[1] )
	sys.exit(2)

while 1:
	linea = arch.readline( )
	if linea == "" :
		break
	if linea[0] == '#' :
		continue

	tks = linea.split( )
	n = len(tks)

	i = 0 
	while i < objs :
		vi = float(tks[i])
		print( vi, end=' ' )
		i += 1

	while i < m :
		vi = int( float(tks[i]) + 0.5 )
		print( vi, end=' ' )
		i += 1

	while i < m+2 :
		vi = int( float(tks[i]) + 0.5 )
		print( vi, end=' ' )
		i += 1

	vi = float(tks[i])
	print( vi, end=' ' )
	i += 1
	print( )
