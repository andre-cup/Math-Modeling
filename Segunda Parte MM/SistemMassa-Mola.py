import matplotlib.pyplot as plt
import drawnow as dr
import numpy as np


k = 5000
m = 2
l = 3
h = 0.0001
to = 0
vo = 0
xo = 2
T = 1
alfa = 0.5
N = 24


vetX = [xo]
vetV = [vo]
vetT = [to]


def make_fig():

    for k in range (N):

        plt.plot((vProximo, 0), (0, 0), color = 'brown') #plot mola
    plt.plot((0, 0), (-0.5, 1), color = 'black')
    plt.plot((0, 6), (-0.3, -0.3), color = 'black')
    plt.plot(xProximo, 1.5, marker='s', markersize=35, color='red')

    plt.axis((-5, 5, -5, 5))
    plt.grid(True)
    plt.show()


#def f_explicito(k, m, l, vo, xo, alfa):
while(to <= T):

    vProximo = vo + (h * (-k/m) * (xo-l)-(2 * (alfa/m))*xo)
    xProximo = xo + (h * vo)

    vo = vProximo
    xo = xProximo

    to += h

    vetT.append(to)
    vetV.append(vo)
    vetX.append(xo)

    dr(make_fig())

#f_explicito(k,m,l,vo,xo,alfa)

'''plt.plot(vetT, vetX, "o", markersize = 2, color = 'red')
plt.plot(vetT, vetV, "o", markersize = 2)
plt.show()
'''