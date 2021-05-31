#Pablo Marroquín, Julio Monzón
#Teoría electromagnética 1, Proyecto
#El programa grafica el campo eléctrico de un dipolo en el origen con cualquier orientación.
#Se utilizó en particular para los dipolos orientados en la dirección de los ejes y para los que contaban con
#un ángulo alfa respecto del eje z

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#Constantes
p = 0.09e-12
e_0 = 8.85e-12
alfa = np.pi/3
beta = 0

a = np.sin(alfa) * np.cos(beta)
b = np.sin(alfa) * np.sin(beta)
c = np.cos(alfa)

k = -p/(4*np.pi*e_0)

#Se construyen los ejes
fig = plt.figure()
ax = fig.gca(projection='3d')

#Se crean los valores de r, theta y phi a utilizar
r_mesh = np.linspace(0.1, 0.3, 6)
theta_mesh = np.linspace(0, np.pi, 23)
phi_mesh = np.linspace(0, 2*np.pi, 5)
#phi_t = [0, np.pi, 0.9*np.pi]
#phi_mesh = np.array(phi_t)

#Se crea la matriz de valores
r, theta, phi = np.meshgrid(r_mesh, theta_mesh, phi_mesh)

#Transformaciones a coordenadas cartesianas
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

#Se construye el campo vectorial
Ax = a*(-2*np.sin(theta)*np.cos(phi)*np.sin(theta)*np.cos(phi) + np.cos(theta)*np.cos(phi)*np.cos(theta)*np.cos(phi) - np.sin(phi)*(-np.sin(phi)))
Bx = b*(-2*np.sin(theta)*np.sin(phi)*np.sin(theta)*np.cos(phi) + np.cos(theta)*np.sin(phi)*np.cos(theta)*np.cos(phi) + np.cos(phi)*(-np.sin(phi)))
Cx = c*(-2*np.cos(theta)*np.sin(theta)*np.cos(phi) - np.sin(theta)*np.cos(theta)*np.cos(phi))

Ay = a*(-2*np.sin(theta)*np.cos(phi)*np.sin(theta)*np.sin(phi) + np.cos(theta)*np.cos(phi)*np.cos(theta)*np.sin(phi) - np.sin(phi)*(-np.cos(phi)))
By = b*(-2*np.sin(theta)*np.sin(phi)*np.sin(theta)*np.sin(phi) + np.cos(theta)*np.sin(phi)*np.cos(theta)*np.sin(phi) + np.cos(phi)*(-np.cos(phi)))
Cy = c*(-2*np.cos(theta)*np.sin(theta)*np.sin(phi) - np.sin(theta)*np.cos(theta)*np.sin(phi))

Az = a*(-2*np.sin(theta)*np.cos(phi)*np.cos(theta) + np.cos(theta)*np.cos(phi)*(-np.sin(theta)))
Bz = b*(-2*np.sin(theta)*np.sin(phi)*np.cos(theta) + np.cos(theta)*np.sin(phi)*(-np.sin(theta)))
Cz = c*(-2*np.cos(theta)*np.cos(theta) - np.sin(theta)*(-np.sin(theta)))

u = (k/r**3)*(Ax + Bx + Cx)
v = (k/r**3)*(Ay + By + Cy)
w = (k/r**3)*(Az + Bz + Cz)

#Se grafica el campo vectorial
ax.quiver(x, y, z, u, v, w, length=0.08)
ax.set_xlabel('X', fontsize=20, rotation=0)
ax.set_ylabel('Y', fontsize=20)
ax.set_zlabel('Z', fontsize=20, rotation=0)

plt.show()


