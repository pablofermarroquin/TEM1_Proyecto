#Pablo Marroquín, Julio Monzón
#Teoría electromagnética 1, Proyecto
#El programa grafica el campo eléctico generado por 2 dipolos a una distancia a que son paralelos al eje z

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#Constantes
a = 2
p1 = 100e-12
p2 = 100e-12
e_0 = 8.85e-12

k1 = -p1/(4*np.pi*e_0)
k2 = -p2/(4*np.pi*e_0)
dif = 0.25

#Se construyen los ejes
fig = plt.figure()
ax = fig.gca(projection='3d')

#Se crean los valores de r, theta y phi a utilizar
r_mesh1 = np.linspace(0, a/2 - dif, 10)
r_mesh2 = np.linspace(a/2 + dif, 1.5, 5)

r_mesh = np.concatenate([r_mesh1, r_mesh2])
theta_mesh = np.linspace(0, np.pi, 23)
phi_mesh = np.linspace(0, 2*np.pi, 5)
#phi = [0,2*np.pi/3, 4*np.pi/3]
#phi_mesh = np.array(phi)

#Se crea la matriz de valores
r , theta, phi = np.meshgrid(r_mesh, theta_mesh, phi_mesh)

#Transformaciones a coordenadas cartesianas
x = r * np.sin(theta) * np.cos(phi) 
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

#Constantes adicionales para reducir longitud de las expresiones del campo
t1 = r**2 + (a**2)/4 - a*r*np.sin(theta)*np.cos(phi)
t2 = r**2 + (a**2)/4 + a*r*np.sin(theta)*np.cos(phi)

#Se construye el campo vectorial
A = np.cos(theta) - (1.5*r*np.cos(theta)*(2*r - a*np.sin(theta)*np.cos(phi)))/(t1)
B = -np.sin(theta) + (1.5*a*r*np.cos(theta)*np.cos(theta)*np.cos(phi))/(t1)
C = (-1.5*a*r*np.cos(theta)*np.sin(phi))/(t1)

D = np.cos(theta) - (1.5*r*np.cos(theta)*(2*r + a*np.sin(theta)*np.cos(phi)))/(t2)
E = -np.sin(theta) - (1.5*a*r*np.cos(theta)*np.cos(theta)*np.cos(phi))/(t2)
F = (1.5*a*r*np.cos(theta)*np.sin(phi))/(t2)

E1x = k1/(t1**(1.5))*(A*np.sin(theta)*np.cos(phi) + B*np.cos(theta)*np.cos(phi) + C*(-np.sin(phi)))
E1y = k1/(t1**(1.5))*(A*np.sin(theta)*np.sin(phi) + B*np.cos(theta)*np.sin(phi) + C*np.cos(phi))
E1z = k1/(t1**(1.5))*(A*np.cos(theta) + B*(-np.sin(theta)))

E2x = k2/(t2**(1.5))*(D*np.sin(theta)*np.cos(phi) + E*np.cos(theta)*np.cos(phi) + F*(-np.sin(phi)))
E2y = k2/(t2**(1.5))*(D*np.sin(theta)*np.sin(phi) + E*np.cos(theta)*np.sin(phi) + F*np.cos(phi))
E2z = k2/(t2**(1.5))*(D*np.cos(theta) + E*(-np.sin(theta)))

u = E1x + E2x
v = E1y + E2y
w = E1z + E2z

#Se grafica el campo vectorial
ax.quiver(x, y, z, u, v, w, length=0.01)
ax.set_xlabel('X', fontsize=20, rotation=0)
ax.set_ylabel('Y', fontsize=20)
ax.set_zlabel('Z', fontsize=20, rotation=0)

plt.show()