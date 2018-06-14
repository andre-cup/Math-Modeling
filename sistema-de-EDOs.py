#Euler explicito terceira questão.


import gc
import matplotlib.pyplot as plt

x = 4
y = 4
t = 0
h = 0.001

fx = -0.16 * x + 0.08 * x * y
gx = 4.5 * y - 0.9 * x * y

vetorX = [x]
vetorY = [y]

while t <= 16:
    y2 = y - h * (gx)
    x2 = x + h
    y = y2
    x = x2

    vetorX.append(x)
    vetorY.append(y)

gc.collect()

plt.plot(t, vetorX)
plt.plot(t, vetorY)
plt.show()