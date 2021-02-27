# Autor: Ciro Fabian Bermudez Marquez
# 02.02.2021

# Librerias
import math
import numpy as np
import collections
import sys

n = len(sys.argv)
if n != 2:
	print("Args: valor inicial")
	sys.exit(1);

nombre = sys.argv[1]

data = np.genfromtxt( nombre )
tam = len(data)  
min_global = -3.224518 
count = 0

for i in range( tam ):
	if abs(data[i] - min_global) < 1e-4 :
		count += 1;



print(count)


	
