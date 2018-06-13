import matplotlib.pyplot as plt

t1 = 0
u1 = 1

variacaoT = 0.1
vetorX = [t1]
vetorY = [u1]

while t1 <= 5:

    u2 = u1 - variacaoT * (u1**3)
    t2 = t1 + variacaoT
    t1 = t2
    u1 = u2

    vetorX.append(t1)
    vetorY.append(u1)

plt.plot(vetorX, vetorY,"o",markersize=2)
plt.show()