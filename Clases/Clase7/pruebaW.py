import numpy as np
import scipy.stats

va = np.genfromtxt( "a.txt" )
print( va.shape )

vb = np.genfromtxt( "b.txt" )
print( vb.shape )

s, p = scipy.stats.wilcoxon( va, vb, correction=True, alternative="less" )
print( s, p )
