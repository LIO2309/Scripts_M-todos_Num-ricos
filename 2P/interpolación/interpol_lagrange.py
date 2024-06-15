"""
Poner puntos
Elegir simplify o no
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
import sympy as sp

# xs: lista de puntos x
# i: indice para el cual el polinomio debe valer 1
# x: la variable donde evaluo

def lagrange_basis(xs, i, x):
    p = 1
    n = len(xs)
    xi = xs[i]
    for k in range(n):
        if k != i:
            xk = xs[k]
            p *= (x - xk) / (xi - xk)
    return p

# ys: lista de puntos y
# xs: lista de puntos x
# x: la variable donde evaluo

def lagrange_interpolation(xs, ys):
    x = sp.symbols('x')
    L = 0
    n = len(xs)
    for k in range(n):
        L += ys[k] * lagrange_basis(xs, k, x)
    #return sp.simplify(L)
    return L

def lagrange_error(xs, f):
    x, phi = sp.symbols('x phi')
    n = len(xs) - 1
    
    # Derivada de orden n+1 de f
    f_sym = f(x)
    f_derivative = sp.diff(f_sym, x, n+1)
    
    # Evaluar la derivada en phi
    f_derivative_phi = f_derivative.subs(x, phi)
    
    # Producto (x - x_i) para i en [0, n]
    product_term = 1
    for xi in xs:
        product_term *= (x - xi)
    
    # Error simbolico
    error = f_derivative_phi / sp.factorial(n+1) * product_term
    return sp.simplify(error)

##### Definir los puntos de interpolacion#####
xs = [0, 1, 2, 3]
ys = [m.cos(0), m.cos(1), m.cos(2), m.cos(3)]

# Definir la funcion a interpolar
def f(x):
    return sp.cos(x)
##############################################

# Calcular el polinomio de interpolacion de Lagrange
lagrange_poly = lagrange_interpolation(xs, ys)
print("Polinomio de interpolacion de Lagrange:")
sp.pretty_print(lagrange_poly)

# Calcular el termino de error simbolico
error_sym = lagrange_error(xs, f)
print("Error simbolico de Lagrange:")
sp.pretty_print(error_sym)

# Graficar la interpolacion y la funcion original
x_vals = np.arange(0, 6, 0.1)
y_vals = [lagrange_interpolation(xs, ys).evalf(subs={sp.symbols('x'): k}) for k in x_vals]

plt.plot(x_vals, y_vals, label='Interpolacion de Lagrange')

x_cos = np.arange(0, 5*np.pi, 0.1)
y_cos = np.cos(x_cos)

plt.plot(x_cos, y_cos, color='green', label='funcion')
plt.legend()
plt.show()
