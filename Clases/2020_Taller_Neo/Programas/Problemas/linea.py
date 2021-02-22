import numpy as np
import matplotlib.pyplot as plt

vx = np.linspace( -3, 10, 20 )
vy = 0.55 * vx + 5.0

fig, ax = plt.subplots( )

ax.plot( vx, vy )
ax.set_xlabel( "x" )
ax.set_ylabel( "f(x)" )
ax.set_title( "Gráfica de la linea f(x) = 0.55x + 5.0" )

plt.show( )
