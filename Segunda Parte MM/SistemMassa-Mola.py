import matplotlib.pyplot as plt
from drawnow import drawnow

k = 5000
m = 2
l = 3
h = 0.0001
to = 0
vo = 0
xo = 2
T = 1
alfa = 1
N = 24


vetX = [xo]
vetV = [vo]
vetT = [to]


def make_fig():
    xo = 0
    dLinhaX = (xProximo - xo) / N

    for k in range (N):
        xk = xo + k * dLinhaX
        plt.plot((xk, xk + 0.099), (-0.1, 0.1), color = 'black') #plot mola
    plt.ylim(-1, 5)
    plt.xlim(-1, 6)
    plt.plot((0, 0), (-0.35, 1), color = 'blue') #linha eixo Y
    plt.plot((0, 6), (-0.35, -0.35), 'k-', color = 'black') #linha eixo X
    plt.plot(xProximo, 0.08, marker='s', markersize=35, color='red') #bloco

    plt.grid(True)

    plt.draw()
    plt.show()

while(to <= T):

    vProximo = vo + (h * (-k/m) * (xo-l)-(2 * (alfa/m))*xo)
    xProximo = xo + (h * vo)

    vo = vProximo
    xo = xProximo

    to += h

    vetT.append(to)
    vetV.append(vo)
    vetX.append(xo)

    drawnow(make_fig())

fig = plt.figure()

'''plt.plot(vetT, vetX, "o", markersize = 2, color = 'red')
plt.plot(vetT, vetV, "o", markersize = 2)
'''