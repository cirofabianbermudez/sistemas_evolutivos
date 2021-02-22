import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import sys

n = len( sys.argv )
if n != 3 :
	print( "Args: data_file c[0/1]" )
	sys.exit(1)

filename = sys.argv[1]
c = int(sys.argv[2])

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
print( A.shape )

A = A.reshape( (600,2) ) 
print( A.shape )

fig, ax = plt.subplots( )

#  = plt.figure(figsize=(5, 4))
# ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1))
ax.set_xlim(-0.5,7.5)
ax.set_ylim(-4.0,12.0)
# ax.set_aspect('equal')
ax.grid()

vx = np.linspace( 0.0, 7.0 )
vy = (vx-2.0)*(vx-5.0) + np.sin( 1.5*np.pi*vx ) 

ax.plot( vx, vy )

if c == 1 :
	vx2 = np.linspace( 2.0, 7.0, 10 )
	vy2 = 5.0 + 2.5*(vx2 - 6.0)
	ax.plot( vx2, vy2 )

points, = ax.plot([], [], 'o', color='r')
time_template = 'generation  %d'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def animate(i):
	a = i*20
	b = (i+1)*20
	points.set_data( A[a:b,0], A[a:b,1] )
	time_text.set_text(time_template % (i+1))
	return points, time_text


fig.canvas.mpl_connect('key_press_event', on_press)
anim = animation.FuncAnimation(
    fig, animate, frames=Itera(30), interval=20, blit=True)
    # fig, animate, len(y), frames=update_time, interval=dt*1000, blit=True)


anim.running = True
anim.direction = +1
plt.show()
