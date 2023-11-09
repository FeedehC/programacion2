import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['image.cmap'] = 'gray'

filas = 10
columnas = 10
#m3 = [[1,2,3],[4,5,6],[7,8,9]]
matriz = [[0]*filas]*columnas
matriz = np.array(matriz)

#matriz = np.zeros((ancho,alto))
#matriz = np.array([0]*(ancho,alto)).reshape(ancho,alto)

plt.imshow(matriz)
#plt.imshow(matriz,vmin=0,vmax=255)
plt.show()

matplotlib.image.imsave("matriz.png",matriz)