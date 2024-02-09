#programa para calcular el  area de un circulo de radio r

import math

# imput
print("------------------------------------")
R = input("ingree el valor del radio del circulo: ")
R = int(R)

# procesing
A = math.pi*R*R
P = 2*math.pi*R

# outpput
print("------------------------------------")
print("EL area del circulo es:" + str(A))
print("EL perimetro del circulo es:" + str(P))
print("------------------------------------")