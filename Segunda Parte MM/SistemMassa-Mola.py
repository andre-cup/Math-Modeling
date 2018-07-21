import matplotlib.pyplot as plt
import drawnow

k = 5000
m = 2
l = 3
h = 0.00001
to = 0
vo = 0
xo = 5
T = 0.5
alfa = 2

vetX = [xo]
vetV = [vo]
vetT = [to]




def func (to):
    while to <= T:

        v2 = vo + (h * (-k/m) * (xo-l)-(alfa/m)*xo)
        x2 = xo + (h * vo)
        vo = v2
        xo = x2
        to += h

        vetT.append(to)
        vetX.append(xo)
        vetV.append(vo)

    print(vetX)
    print(vetV)

    drawnow(vetX, vetV)

    return vetX, vetV

plt.plot(vetX, vetV, marker='s', markersize=35, color='blue')
plt.show()

