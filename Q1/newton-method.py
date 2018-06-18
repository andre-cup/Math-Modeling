#Método de Newton primeira questão.



import math

x = 0.8
flag = True
raiz = []

while flag == True:
    fx = (math.exp(x)) - 2.0
    derivadaFunc = math.exp(x)
    xProxK = x - (fx / derivadaFunc)
    raiz.append(xProxK)

    if abs(xProxK - x) <= 0.01:
        break
    else:
        x = xProxK

print(raiz)