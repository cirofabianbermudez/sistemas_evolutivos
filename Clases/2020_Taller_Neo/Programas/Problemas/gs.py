# Función lineal con respecto a los coeficientes
# pero usa funciones básicas no lineales
#
# Fraga 11.11.2020
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

vx = np.linspace( -3, 5, 30 )
vy = np.linspace( -3, 5, 30 )

xx, yy = np.meshgrid( vx, vy )

z = np.empty( xx.shape )
n = xx.shape[0]

i = 0
while i < n :
	j = 0
	while j < n :
		z[i,j] = 0.8*np.exp( -(xx[i,j] - 1.0)**2 ) + 0.2 * np.exp( -(yy[i,j] - 4.0)**2 )
		j += 1
	i += 1

fig, ax = plt.subplots( )

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.plot_surface( xx, yy, z, cmap=cm.coolwarm, linewidth=0 )

plt.show( )
