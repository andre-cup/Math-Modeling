import matplotlib.pyplot as plt
from drawnow import *
import numpy as np

k = 5000
m = 2
l = 3
h = 0.00001
to = 0
vo = 0
xo = 2
T = 0.5
alfa = 5

vetX = [xo]
vetV = [vo]
vetT = [to]

#def make_fig():

#plt.plot(2, 4, marker='s', markersize=35, color='red')
plt.plot((0.6, 0.8), (1.3, 1.8), )
plt.axis((0, 10, 0, 10))
plt.grid(True)
plt.show()


'''def f_explicito(k, m, l, vo, xo, alfa):

    while(to <= T):

        vProximo = vo + (h * (-k/m) * (xo-l)-(alfa/m)*xo)
        xProximo = xo + (h * vo)

        vo = vProximo
        xo = xProximo



#plt.plot(0, 5, marker='s', markersize=35, color='blue')
#plt.show()

#def range_kutta():
'''