import numpy as np

X = np.genfromtxt("sale.txt")

m = len( X )

s = 0
i = 0
while i < m :
	if X[i] >= 70.0 :
		s += 1
	i += 1

print( "Son", s, "números >= 70" )
