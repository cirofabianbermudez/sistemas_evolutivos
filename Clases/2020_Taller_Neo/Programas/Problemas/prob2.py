import numpy as np
import matplotlib.pyplot as plt

vx = np.linspace( 0, 7, 200 )
vy = (vx-2.0)*(vx-5.0) + np.sin( 1.5* np.pi * vx )
vyder = 2.0*vx - 7.0 + 1.5*np.pi * np.cos( 1.5*np.pi*vx )

fig, ax = plt.subplots( )

ax.plot( vx, vy )
ax.plot( vx, vyder )
ax.set_xlabel( "x" )
ax.set_ylabel( "f(x) o f'(x)" )
ax.set_title( "Gráfica del problema no lineal" )
# ax.grid()

plt.show( )
