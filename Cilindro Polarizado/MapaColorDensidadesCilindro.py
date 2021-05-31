import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES
alpha0 = 10
k = 10**(-6)#100
a = 4
b = 8

#DEFINICION DE DIMENSIONES
s = np.linspace(0.001, 10, 1000)
phi = np.linspace(0, 2 * np.pi, 1000)
r, th = np.meshgrid(s, phi)

#DENSIDADES SUPERFICIALES
Sigma_a=-k*np.exp(-a**2/alpha0)
Sigma_b=k*np.exp(-b**2/alpha0)

#DENSIDAD VOLUMETRICA
def Rho(x):
    return -k*np.exp(-x**2/alpha0)*(1-(2*x**2)/alpha0)/x
    

densidad=[]
j=0

while j<1000:
    dens_i =[]
    for i in range(0,1000):
        if s[i] < (a-0.08):
            dens_i.append(0)
        else:
            if s[i] >= (a-0.08) and  s[i] < (a+0.08):
                dens_i.append(Sigma_a)    
            else:
                if s[i] > (b-0.08) and  s[i] < (b+0.08):
                    dens_i.append(Sigma_b)
                else:
                    if s[i] > (b+0.08):
                        dens_i.append(0)
                    else:
                        dens_i.append(Rho(s[i]))
    densidad.append(dens_i)
    j+=1
    
#CONFIGURACIONES DE GRAFICAS
plt.subplot(projection="polar")
plt.pcolormesh(th, r, densidad, shading="auto",cmap="rainbow")
plt.colorbar()
plt.grid()
plt.show()
    
