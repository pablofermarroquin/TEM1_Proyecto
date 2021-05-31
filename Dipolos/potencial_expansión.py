#Pablo Marroquín, Julio Monzón
#Teoría electromagnética 1, Proyecto
#El programa construye las superficies equipotenciales para la densidad de carga del último problema de dipolos
#Comentando líneas de código puede decidirse si se trabaja con potenciales cercanos o lejanos del origen

import plotly.graph_objects as go
import numpy as np

#Constantes
e_0 = 8.85e-12
k = 1/(4*np.pi*e_0)
n = 20 #20. Utilizar 3 para cerca al origen y 20 para lejos
r = 80j

#Se construyen los valores de x,y,z
X, Y, Z = np.mgrid[-n:n:r, -n:n:r, -n:n:r]

#Equivalencia de coordenadas esféricas y cartesianas
R = (X**2 + Y**2 + Z**2)**(1/2)

#Valores que tomarán las equipotenciales. La expresión se trasladó a coordenadas cartesianas
#Utilizar la primera si se quiere potencial lejos del origen y la segunda para potenciales cercanos al origen
values = k*((1/R) - (6/R**3)*((3*((Z**2)/(R**2))-1)/2))
#values = k*(0.25 - ((R**2)/120)*((3*((Z**2)/(R**2))-1)/2))

#Se grafican las equipotenciales
fig= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    opacity = 0.3,
    isomin= 5e8,#5e8, Utilizar 2.17e9 para cerca del origen y 5e8 para lejos
    isomax= 8e8,#8e8, Utilizar 2247951174 para cerca del origen y 8e8 para lejos
    surface_count=5, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=5, # colorbar ticks correspond to isosurface values
    
    caps=dict(x_show=False, y_show=False)
))

fig.show()