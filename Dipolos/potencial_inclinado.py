#Pablo Marroquín, Julio Monzón
#Teoría electromagnética 1, Proyecto
#El programa grafica 6 superficies equipotenciales para los dipolos centrados en el origen con cualquier orientación

import plotly.graph_objects as go
import numpy as np

#Constantes
p = 1e-12
e_0 = 8.85e-12
k = p/(4*np.pi*e_0)
alfa = (3/4)*np.pi
beta = 0

#Se construyen los valores de x,y,z
X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

#Equivalencia de coordenadas esféricas y cartesianas
R = (X**2 + Y**2 + Z**2)**(1/2)

#Valores que tomarán las equipotenciales. La expresión se trasladó a coordenadas cartesianas
values = k/(R**3)*(X*np.sin(alfa)*np.cos(beta) + Y*np.sin(alfa)*np.sin(beta) + Z*np.cos(alfa))

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