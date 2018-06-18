import math
import matplotlib.pyplot as plt

h = 0.001
x = 0
y = 3

vetorAnaliticoX = []
vetorAnaliticoY = []
vetorExplicitoX = []
vetorExplicitoY = []
vetorRungeKuttaX = []
vetorRungeKuttaY = []

#Metodo Analitico
while x <= 3:

    yAnalitico = math.exp(-x) + 2 * math.exp(-2 * x)
    x += h

    vetorAnaliticoY.append(yAnalitico)
    vetorAnaliticoX.append(x)

#Metodo de Euler Explicito

x = 0
y = 3

while x <= 3:

    yDeX = math.exp(-x) - 2 * y
    y2 = y + h * yDeX
    x2 = x + h
    y = y2
    x = x2

    vetorExplicitoX.append(x)
    vetorExplicitoY.append(y)

#Metodo de Runge-Kutta

x = 0
y = 3

while x <= 3:

    fx = math.exp(-x)
    fy = - 2 * y

    Kn1 = fx + fy
    Kn2 = fx + (h/2) + fy + ((h/2) * Kn1)
    Kn3 = fx + (h/2) + fy + ((h/2) * Kn2)
    Kn4 = fx + h + fy + (h * Kn3)

    yProximo = y + h/6 * (Kn1 + (2 * Kn2) + (2 * Kn3) + Kn4)
    x += h

    y = yProximo

    vetorRungeKuttaX.append(x)
    vetorRungeKuttaY.append(y)

plt.title("Grafico - Q2")
plt.plot(vetorAnaliticoX, vetorAnaliticoY, markersize = 1, color = "blue")
plt.plot(vetorExplicitoX, vetorExplicitoY,"--",markersize = 1, color = "red")
plt.plot(vetorRungeKuttaX, vetorRungeKuttaY,"-.",markersize = 1, color = "green")
plt.show()