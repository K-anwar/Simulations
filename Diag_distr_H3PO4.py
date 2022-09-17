import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 14, 60)
y1 = 1/(1+ 10**(x-2.15) + 10**(2*x-9.35) + 10**(3*x-21.45))
y2 = y1 * 10**(x-2.15) 
y3 = y1 * 10**(2*x-9.35)
y4 = y1 * 10**(3*x-21.45)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
