#Euler explicito terceira questão.
import gc
import matplotlib.pyplot as plt

t = 0
h = 0.001

x = 4
y = 4

vetorX = [x]
vetorY = [y]

tN = [t]

fx = -0.16 * x + 0.08 * x * y
gx = 4.5 * x - 0.9 * x * y


while t <= 16:


    x2 = x + h * fx
    y2 = y + h * gx

    x = x2
    y = y2

    t += h

    vetorX.append(x)
    vetorY.append(y)
    tN.append(t)

plt.plot(tN, vetorX, markersize = 1, color = "blue")
plt.plot(tN, vetorY,"--", markersize = 1, color = "green")

plt.show()
