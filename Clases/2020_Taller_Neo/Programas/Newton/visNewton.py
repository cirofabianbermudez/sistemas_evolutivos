import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import sys

n = len( sys.argv )
if n != 2 :
	print( "Args: data_file" )
	sys.exit(1)

filename = sys.argv[1]

class Itera:
	"""Iterator for looping over a sequence backwards."""
	def __init__(self, data):
		self.index = 0 
		self.n = data

	def __iter__(self):
		return self

	def __next__(self):
		self.index = self.index + anim.direction
		if self.index >= self.n :
			self.index = 0

		if self.index < 0 :
			self.index = self.n - 1

		return self.index

	def next( self ) :
		self.__next__( )


def on_press(event):
	if event.key.isspace():
		if anim.running:
			anim.event_source.stop()
		else:
			anim.event_source.start()
		anim.running ^= True
	elif event.key == 'left':
		anim.direction = -1
	elif event.key == 'right':
		anim.direction = +1

	# Manually update the plot
	if event.key in ['left','right']:
	 	# t = anim.frame_seq.next( )
	 	# t = anim.direction
		# anim.new_frame_seq( )
		# anim.frames( )
		# anim._draw_next_frame( )
		anim._step( )
		#plt.draw()	# 	update_plot(t)



A = np.fromfile( filename )
n = len( A )
print( n )

n /= 3
A = A.reshape( (int(n),3) ) 
print( A.shape )

fig, ax = plt.subplots( )

#  = plt.figure(figsize=(5, 4))
# ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1))
ax.set_xlim(-0.2,7.2)
ax.set_ylim(-11.0,11.0)
# ax.set_aspect('equal')
ax.grid()

vx = np.linspace( 0.0, 7.0, 150 )
vy = (vx-2.0)*(vx-5.0) + np.sin( 1.5*np.pi*vx ) 
vyder = 2.0*vx - 7.0 + 1.5*np.pi * np.cos( 1.5*np.pi*vx )

vxlinea = np.linspace( 0.0, 7.0, 10 )
ax.plot( vx, vy )
ax.plot( vx, vyder )

punto, = ax.plot([], [], 'o', color='r')
linea, = ax.plot([], [], color='r')
time_template = 'Iteración  %d'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def animate(i):
	# ax.scatter( A[i,0], A[i,1] )
	vylinea = A[i,2] * (vxlinea-A[i,0]) + A[i,1]
	punto.set_data( A[i,0], A[i,1] )
	linea.set_data( vxlinea, vylinea )
	time_text.set_text(time_template % (i+1))
	return punto, linea, time_text


fig.canvas.mpl_connect('key_press_event', on_press)
anim = animation.FuncAnimation(
    fig, animate, frames=Itera(int(n)), interval=1000, blit=True)
    # fig, animate, len(y), frames=update_time, interval=dt*1000, blit=True)


anim.running = True
anim.direction = +1
plt.show()
