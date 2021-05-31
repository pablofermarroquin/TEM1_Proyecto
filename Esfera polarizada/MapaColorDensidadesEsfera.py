import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES

k = 0.1    #10**(2)#100
Q= -1e-6
a = 2.23e-4
b = 4.46e-4
Epsilon0=8.85*10**(-12)
Epsilon_r=2.28

#DEFINICION DE DIMENSIONES
s = np.linspace(0.0, 4.5*a, 1000)
phi = np.linspace(0.0, 2 * np.pi, 1000)
r, th = np.meshgrid(s, phi)

#DENSIDADES SUPERFICIALES
#Sigma_a_dentro=Q/(4*np.pi*a**2)
Sigma_a_fuera=-Q/(4*np.pi*a**2)*(1-1/Epsilon_r)
Sigma_b_dentro=Q/(4*np.pi*b**2)*(1-1/Epsilon_r)
Sigma_b_fuera=k*b
Sigma_2b_fuera=-2*k*b
Rho_a_b=0
Rho_b_2b=3*k


#DENSIDAD VOLUMETRICA
#def Rho_b_2b(x):
 #   return -k*np.exp(-x**2/alpha0)*(1-(2*x**2)/alpha0)/x   

densidad=[]
j=0
ancho=0.2e-4
while j<1000:
    dens_i =[]
    for i in range(0,1000):
        if (s[i] < (a)):
            dens_i.append(0)
        elif (s[i]>a and s[i]<a+ancho):
            dens_i.append(Sigma_a_fuera)
        elif (s[i]>a+ancho and s[i]<b-ancho):
            dens_i.append(Rho_a_b)
        elif (s[i]>b-ancho and s[i]<b):
            dens_i.append(Sigma_b_dentro)
        elif (s[i]>b and s[i]<b+ancho):
            dens_i.append(Sigma_b_fuera)
        elif (s[i]>b+ancho and s[i]<2*b-ancho):
            dens_i.append(Rho_b_2b)
        elif (s[i]>2*b-ancho and s[i]<2*b):
            dens_i.append(Sigma_2b_fuera)
        else:
            dens_i.append(0)
    densidad.append(dens_i)
    j+=1
    
#CONFIGURACIONES DE GRAFICAS
plt.subplot(projection="polar")
plt.pcolormesh(th, r, densidad, shading="auto",cmap="rainbow")
plt.colorbar()
plt.grid()
plt.show()
    
