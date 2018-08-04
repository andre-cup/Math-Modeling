import matplotlib.pyplot as plt
import numpy as np

E = 10.0 # Tensao constante da fonte
C = 0.000001 # Capacitancia
R = 2000.0 # Resistencia

### Condicao inicial ###

t0 = 0.0 # tempo incial
q0 = 0.0 # carga inicial

h = 0.000001

### Tempo maximo da simulacao ###

M = 6*R*C

vetQ = [q0]
vetT = [t0]

while(t0 < M):

    E1 =
    t1 = t0 + h
    q0 = q1
    t0 = t1

    t0 += h

    vetQ.append(q0)
    vetT.append(t0)

plt.plot(vetQ, vetT, "o", markersize = 2)
plt.show()