#Euler explicito terceira questão.
import gc
import matplotlib.pyplot as plt

t = 0
h = 0.001

x = 4
y = 4
xg = 4
yg = 4
vetorXf = [x]
vetorYf = [y]

vetorXg = [xg]
vetorYg = [yg]
tN = [t]

while t <= 16:
    fx = -0.16 * x + 0.08 * x * y
    gx = 4.5 * x - 0.9 * x * y

    xg2 = xg + h
    yg2 = yg - h * (y **3)

    xf2 = x + h
    yf2 = y - h * (yg **3)

    x = xf2
    y = yf2
    xg = xg2
    yg = yg2

    t += h

    vetorXf.append(x)
    vetorYf.append(y)
    vetorXg.append(xg)
    vetorYg.append(yg)
    tN.append(t)

plt.plot(tN, vetorXf, vetorYf, markersize = 1, color = "blue")
plt.plot(tN, vetorXg, vetorYg,"--", markersize = 1, color = "green")

plt.show()
