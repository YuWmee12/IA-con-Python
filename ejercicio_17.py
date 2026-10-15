import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#INTERPOLACIÓN LINEAL
# Datos de ejemplo
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Crear una función de interpolación
interpolacion_lineal = interp1d(x, y, kind='linear')

# Generar nuevos valores de x para interpolar
x_nuevo = np.linspace(0, 4, 50)
y_nuevo = interpolacion_lineal(x_nuevo)

# Graficar los datos originales y la interpolación
plt.plot(x, y, 'o', label='Datos Originales')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación Lineal')
plt.legend()
plt.show()
