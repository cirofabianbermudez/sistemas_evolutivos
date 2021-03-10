import sys
import math

n = len( sys.argv )
if n != 3 :
	print( "Args: m h" )
	sys.exit(1)

m = int(sys.argv[1])
h = int(sys.argv[2])

# The number of vectors is calculated 
c = math.factorial( m+h-1)/(math.factorial( m-1 )*math.factorial( h ))
print( "# ", c, "vectors with m =", m, ", h =", h )

# A vector is calculated each time
x = [0]*m   # It uses integer numbers
x[0] = h

j = 0
while x[m-1] < h :
	i = 0   # print the vector
	while i < m :
		v = float(x[i])/h
		print( v, end=' ' )
		i += 1
	print( )
	x[j] -= 1	
	if j < m-2 :
		v = 0
		i = 0
		while i <= j :
			v += x[i]
			i += 1
		x[j+1] =  h-v
		i = j+2
		while i < m :
			x[i] = 0
			i += 1
		j += 1
	else :
		x[m-1] += 1
	
	k = -1
	i = 0
	while i < m - 1 :
		if x[i] > 0 :
			k = i
		i += 1

	if k >= 0 :
		j = k

i = 0   # Print the last vector
while i < m :
	v = float(x[i])/h
	print( v, end=' ' )
	i += 1
print( )
