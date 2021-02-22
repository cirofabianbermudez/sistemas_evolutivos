class Punto :
	def __init__( self, x, y ) :
		self.x = x
		self.y = y

	def __add__( self, A ) :
		return  Punto( self.x+A.x, self.y + A.y )

	def print( self ) :
		print( self.x, self.y )
