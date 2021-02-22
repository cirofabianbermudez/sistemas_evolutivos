import math

def f1(x):
	v = (x-2.0)*(x-5.0) + math.sin( 1.5*math.pi*x )
	return v

def df1(x):
	v = 2.0*x - 7.0 + 1.5*math.pi * math.cos( 1.5*math.pi*x )
	return v

def ddf1(x):
	v = 2.0 - 1.5*math.pi*1.5*math.pi * math.sin( 1.5*math.pi*x )
	return v
