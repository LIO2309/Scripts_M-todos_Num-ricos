"""
1) definir funcion a integrar
2) definir límites de integraciòn
"""

import math

def gauss_two_point(func, a, b): #Precisi�n 3
    x0 = (a + b) / 2 - (1 / math.sqrt(3)) * ((b - a) / 2)
    x1 = (a + b) / 2 + (1 / math.sqrt(3)) * ((b - a) / 2)
    return (b - a) / 2 * (func(x0) + func(x1))

def gauss_three_points(f, a, b): #Precisi�n 5
    x0 = (a + b) / 2 - (math.sqrt((3/5)) * (b - a) / 2)
    x1 = (a + b) / 2
    x2 = (a + b) / 2 + (math.sqrt((3/5)) * (b - a) / 2)

    integral_approximation = ((b - a) / 18) * (5 * f(x0) + 8 * f(x1) + 5 * f(x2))
    return integral_approximation


########################################

a = -1  #limite de integracion inferior
b = 1  #limite de integracion superior

def f(x):
    #if(x == 0):
    #    return 1   #Usar en el caso sin(x)/x para salvar la indeterminaci�n
    return 1 + x + x**2 + x**3 + x**4

########################################

# Test the gauss_two_point function
approximation_two_point = gauss_two_point(f, a, b)
print("Approximation using two-point Gauss-Legendre:", approximation_two_point)

# Test the gauss_three_points function
approximation_three_points = gauss_three_points(f, a, b)
print("Approximation using three-point Gauss-Legendre:", approximation_three_points)

