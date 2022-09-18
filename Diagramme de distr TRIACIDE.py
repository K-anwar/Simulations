import matplotlib.pyplot as plt
import numpy as np

pk1, pk2, pk3 = float(input()), float(input()), float(input())

x = np.linspace(0, 14, 60)
y1 = 1/(1+ 10**(x-pk1) + 10**(2*x-(pk1+pk2)) + 10**(3*x-(pk1+pk2+pk3)))
y2 = y1 * 10**(x-pk1) 
y3 = y1 * 10**(2*x-pk1-pk2)
y4 = y1 * 10**(3*x-pk1-pk2-pk3)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
