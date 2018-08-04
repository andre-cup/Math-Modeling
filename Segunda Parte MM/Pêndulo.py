import numpy as np
import matplotlib as plt

g = 9.8
L = 0.15 # comprimento do pêndulo
alpha = 1.0 # constante de amortecimento
t0= 0.0 # instante de tempo inicial
theta_graus = 90 # posição angular inicial (em graus)
theta0 = theta_graus* (3.14/180) #(conversão para radianos)
w0= 0 # velocidade angular inicial
h = 0.0001

vetW = [w0]
vetTheta = [theta0]
vetT = [t0]

while(t0 <= 0.5):

    wLinha = w0 + h * (-g/L * np.sin(theta_graus))
    thetaLinha = w0 + h
    w0 = wLinha
    theta_graus = thetaLinha


    t0 += h
