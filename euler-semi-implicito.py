import matplotlib.pyplot as plt

epsylon = 0.001
deltaT = 0.1
tN = 0
uN = 1
teta = 0.5
vetorX = [tN]
vetorY = [uN]


while tN <= 5:
    uNProx = uN
    E = epsylon + 1

    while E > epsylon:
        uNProxK = uNProx - (uNProx - uN + deltaT*(1-teta)*(uN**3) + teta*(uNProx**3))/(1 + 3*teta*deltaT*(uNProx**2))

        E = abs(uNProxK - uNProx)
        uNProx = uNProxK

    uProx = uNProxK
    tProx = tN + deltaT
    uN = uProx
    tN = tProx
    vetorX.append(tN)
    vetorY.append(uN)

plt.plot(vetorX, vetorY)
plt.show()