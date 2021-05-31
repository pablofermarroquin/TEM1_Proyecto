import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES

k = 0.1#1e-9#1e-10#1e-9#10**(2)#100
Q=-1e-6#-8.04e-7
R100=9.26e-3
b = R100/2 #3.0e-3#2#4.31#2
a=R100/4#1.5e-3#1#2.15#1
Epsilon0=8.85e-12
Epsilon_r=2.28

#DEFINICION DE DIMENSIOENS
r = np.linspace(0, 6*a, 100000)
#r=r*10**(-4)


E=[] #Desplazamiento

for i in range(0,100000):
    if( r[i] < a):
        E.append(0)
    elif ( r[i]< b and r[i]>=a):
        E.append(Q/(4*np.pi*Epsilon0*Epsilon_r*r[i]**2))
    elif ( r[i]<= 2*b+2e-7 and r[i]>=b):
        campo=( Q/(4*np.pi*Epsilon0*r[i]**2) ) +k*r[i]/Epsilon0 
        E.append(  campo )
        #Se obtiene E=0.10531965227016826 cuando r[i]=3.9998999899989998
        if(campo>0):
            print(str(campo)+" "+str(r[i]))
    elif ( r[i]>2*b+2e-7):
        E.append(Q/(4*np.pi*Epsilon0*r[i]**2))

 
plt.ylabel("Campo electrico (V/m)")
plt.xlabel("Distancia radial (m)")
plt.plot(r/10,E,c="g")
plt.title("\nCampo electrico vrs. distancia radial") 
