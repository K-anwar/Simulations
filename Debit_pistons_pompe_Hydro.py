import numpy as np
import matplotlib.pyplot as plt


#Q(teta) = e * dteta <-sin(teta)>+ 

A = 2.5 # e. dTeta

def Q(teta):
    return - A * np.sin(teta) if np.sin(teta)<0 else 0
        
x = np.linspace(0, 2*np.pi, 200)
yy = []

n = 6
for i in range(n):
    step = 2*np.pi/n
    yy.append( [Q(j-i*step) for j in x]) 


for p in yy:
    plt.plot(x, p)

plt.xlabel("Teta")
plt.ylabel("Débit Instantané Q(Teta)")
plt.title("Graph de Débit géneré par six pistons d'une pompe Hydraulique.")

plt.show()

