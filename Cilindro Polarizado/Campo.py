
import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES
alpha0 = 10
k = 10**(-6)#100
a = 4
b = 8
Epsilon0=8.85*10**(-12)

#DEFINICION DE DIMENSIOENS
s = np.linspace(0.001, 9, 1000)

#CAMPO ELECRICO
def E(x):
    return -k*np.exp(-(x**2)/alpha0)/Epsilon0

Campo=[]

for i in range(0,1000):
    if( s[i] < a or s[i]>b):
        Campo.append(0)
    else:
        Campo.append(E(s[i]))


plt.ylabel("Campo electrico (V/m)")
plt.xlabel("Distancia radial (m)")
plt.plot(s,Campo,c="g")
plt.title("\nCampo electrico vrs. distancia radial")  
