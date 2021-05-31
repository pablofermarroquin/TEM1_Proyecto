import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES
#k = 10**(-6)#100
Q=1e-6
a = 2.23e-4
b = 4.46e-4
Epsilon0=8.85*10**(-12)

#DEFINICION DE DIMENSIOENS
r = np.linspace(0.001, 10, 1000)
r=r*10**(-4)


D=[] #Desplazamiento

for i in range(0,1000):
    if( r[i] < a):
        D.append(0)
    else:
        D.append(Q/(4*np.pi*r[i]**2))


plt.ylabel("Desplazamiento electrico (C/m²)")
plt.xlabel("Distancia radial (m)")
plt.plot(r,D,c="g")
plt.title("\nDesplazamiento electrico vrs. distancia radial") 