import numpy as np
import matplotlib.pyplot as plt

vx = np.linspace( 0, 7 )
vy = (vx-2.0)*(vx-5.0) + np.sin( 1.5* np.pi * vx )

fig, ax = plt.subplots( )

ax.plot( vx, vy )
ax.set_xlabel( "x" )
ax.set_ylabel( "f(x)" )
ax.set_title( "Gráfica del problema no lineal" )

plt.show( )
