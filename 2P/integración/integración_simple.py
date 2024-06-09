"""
1)definir funcion a integrar
2) definir limites de integracion
"""


def integr_por_izq(fun,a,b): # Precisi�n 0
    return fun(a) * (b-a)
def integr_por_der(fun,a,b):  # Precisi�n 0 
    return fun(b) * (b-a)

def intgr_punto_medio(fun,a,b): #Precisi�n 1
    return fun((a+b)/2)*(b-a) 

def trapezoidal_rule(func, a, b): #Precisi�n 1
    return (b-a) * 0.5 * (func(b)+func(a))
 

def simpsons_one_third_general(func, a, b, n):
    """Approximate the definite integral of a function using Simpson's 1/3 Rule.

    Parameters:
    func : function
        The function to be integrated.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of subintervals (should be even) for approximation.

    Returns:
    float
        The approximate value of the definite integral.
    """
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

def simpsons_three_eighth_general(func, a, b, n):
    """Approximate the definite integral of a function using Simpson's 3/8 Rule.

    Parameters:
    func : function
        The function to be integrated.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of subintervals (should be multiple of 3) for approximation.

    Returns:
    float
        The approximate value of the definite integral.
    """
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


def simpsons_three_eighth(func, a,b): #Precisi�n 3 
    return simpsons_three_eighth_general(func, a, b, 3)

def simpsons_one_third(func, a, b): #Precisi�n 3
    return simpsons_one_third_general(func, a,b ,2)




def print_all_aprox(func, a, b):
    print("Por izquierda:\t\t ", integr_por_izq(func, a,b))
    print("Por derecha:\t\t ", integr_por_der(func, a,b))
    print("Por el medio:\t\t ", intgr_punto_medio(func,a,b))
    print("Regla del trapecio:\t ", trapezoidal_rule(func, a,b))
    print("Simpson 1/3:\t\t ", simpsons_one_third(func,a,b))
    print("Simpson 3/8 ;\t\t ", simpsons_three_eighth(func,a ,b))

import math
    
####################################################################

def f(x):
    #if(x == 0):
        #return 1       #Usar en el caso sin(x)/x para salvar la indeterminaci�n
    return math.sin(x)

a = 0       #limite de integración inferior
b = math.pi #limite de integración superior

####################################################################

print_all_aprox(f, a, b)

