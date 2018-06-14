## Euler explicito segunda questão.


import math
import matplotlib.pyplot as plt

class Questao2():

    h = 0.001
    x = 0
    y = 3

    def funcExplicita (self):


        vetorX = []
        vetorY = []


        while x <= 3:
            yDeX = math.exp(-x) + 2*math.exp(-2*x)
            y2 = y - self.h * (y**3)
            x2 = x + self.h
            y = y2
            x = x2

            vetorX.append(x)
            vetorY.append(y)

        plt.plot([vetorX, vetorY],)
        plt.show()

    def rungeKutta(self):
