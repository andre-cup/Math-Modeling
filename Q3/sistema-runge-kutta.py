import gc
import matplotlib.pyplot as plt

x = 4
y = 4
t = 0
h = 0.001

vetorY = [y]
vetorX = [x]
tN = [t]

while t <= 16:

    fx = -0.16 * x
    fxy = 0.08 * x * y
    gx = 4.5 * x
    gxy = - 0.9 * x * y

    fxH = -0.16 * x + (h / 2) + 0.08 * x * y + (h / 2)
    gxH = 4.5 * x + (h / 2) - 0.9 * x * y + (h / 2)


    Kn11 = fx + fxy
    Kn21 = gx + gxy

    Kn12 = fxH * Kn11
    Kn22 = gxH * Kn11

    Kn13 = fxH * Kn12
    Kn23 = gxH * Kn12

    Kn14 = fx * Kn13
    Kn24 = gx * Kn13

    xProximo = x - h/6 * (Kn11 + (2 * Kn12) + (2 * Kn13) + Kn14)
    yProximo = y - h/6 * (Kn21 + (2 * Kn22) + (2 * Kn23) + Kn24)

    x = xProximo
    y = yProximo

    t += h

    vetorX.append(x)
    vetorY.append(y)
    tN.append(t)

plt.plot(tN, vetorX, markersize = 1, color = "blue")
plt.plot(tN, vetorY,maker = 's', markersize = 1, color = "green")
plt.show()