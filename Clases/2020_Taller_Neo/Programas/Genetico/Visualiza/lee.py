import numpy as np

A = np.fromfile( "g1.bin" )
print( A.shape )

A = A.reshape( (600,2) ) 
print( A.shape )
