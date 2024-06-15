def trapezoidal_rule_compuesta(func, a, b, n):
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2  # Start with the endpoints
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

#simpson compuesta es la general 

def integr_por_izq(fun, a, b, n):
    h = (b - a) / n
    approx = sum(fun(a + i * h) for i in range(n)) * h
    return approx

def integr_por_der(fun, a, b, n):
    h = (b - a) / n
    approx = sum(fun(a + (i + 1) * h) for i in range(n)) * h
    return approx



def simpsons_one_third(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals must be even for Simpson's 1/3 Rule")

    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral

def simpsons_three_eighth(func, a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule")

    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            integral += 2 * func(x)
        else:
            integral += 3 * func(x)

    integral *= 3 * h / 8
    return integral


def regla_punto_medio(funcion, a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(n):
        x_i = a + (i + 0.5) * h
        suma += funcion(x_i)
    integral = h * suma
    return integral



def print_all_integration_methods(func, a, b, n):
    print("Trapezoidal Rule (Composite):", trapezoidal_rule_compuesta(func, a, b, n))
    print("Left Rectangle (Composite):", integr_por_izq(func, a, b, n))
    print("Punto medio (Composite):", regla_punto_medio(func, a, b, n))
    print("Right Rectangle (Composite):", integr_por_der(func, a, b, n))
    try:
        print("Simpson 3/8  (Composite):", simpsons_three_eighth(func, a, b, n))
    except ValueError as e:
        print(e)
    try:
        print("Simpson 1/3 (Composite):", simpsons_one_third(func, a, b, n))
    except ValueError as e:
        print(e)

import math
 
########################################

a = 0  #limite de integracion inferior
b = 1  #limite de integracion superior

intervalos = 4 #número de intervalos

def f(x):
    #if(x == 0):
    #    return 1
    return 0.2 + 25*x + 3*x**2 + 2*x**2

########################################


print_all_integration_methods(f, a, b, 4)
