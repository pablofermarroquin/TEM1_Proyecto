#Pablo Marroquín, Julio Monzón
#Teoría electromagnética 1, Proyecto
#El programa grafica las superficies equipotenciales para los dipolos paralelos al eje z

import plotly.graph_objects as go
import numpy as np

#Constantes
p1 = 1e-12
p2 = 1e-12
a = 4

e_0 = 8.85e-12

k1 = p1/(4*np.pi*e_0)
k2 = p2/(4*np.pi*e_0)

#Se construyen los valores de x,y,z
X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

#Equivalencia de coordenadas esféricas y cartesianas
R = (X**2 + Y**2 + Z**2)**(1/2)

#Valores que tomarán las equipotenciales. La expresión se trasladó a coordenadas cartesianas
V1 = k1*(Z)/((R**2 + (a**2)/4 - a*X)**(3/2))
V2 = k2*(Z)/((R**2 + (a**2)/4 + a*X)**(3/2))

values = V1 + V2

#Se grafican las equipotenciales
fig= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    opacity = 0.6,
    isomin=-1e-3,
    isomax=1e-3,
    surface_count=6, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=6, # colorbar ticks correspond to isosurface values
    
    caps=dict(x_show=False, y_show=False)
))

fig.show()