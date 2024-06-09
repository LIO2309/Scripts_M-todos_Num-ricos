import numpy as np
import math as m
import matplotlib.pyplot as plt
import sympy as sp

def divided_differences(x, y):
    """
    Compute the divided differences table.

    Args:
    x (list): List of x-coordinates.
    y (list): List of y-coordinates.

    Returns:
    list: Divided differences table.
    """
    n = len(x)
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])

    return F

def newton_interpolation(x, y, xi):
    """
    Perform Newton interpolation.

    Args:
    x (list): List of x-coordinates.
    y (list): List of y-coordinates.
    xi (float): The point to interpolate at.

    Returns:
    float: Interpolated value at xi.
    """
    n = len(x)
    F = divided_differences(x, y)
    interpolation = F[0][0]
    factor = 1.0

    for i in range(1, n):
        factor *= (xi - x[i - 1])
        interpolation += factor * F[0][i]

    return interpolation

##### Definir los puntos de interpolacion#####
xs = [0, 1, 2, 3]
ys = [m.cos(0), m.cos(1), m.cos(2), m.cos(3)]

# Definir la funcion a interpolar
def f(x):
    return sp.cos(x)
##############################################

# Calcular el polinomio de interpolacion de Newton
x = sp.symbols('x')
newton_poly = newton_interpolation(xs, ys, x)
print("Polinomio de interpolacion de Newton:")
sp.pretty_print(newton_poly)

# Graficar la interpolacion y la funcion original
x_vals = np.arange(0, 6, 0.1)
y_vals = [newton_interpolation(xs, ys, k) for k in x_vals]

plt.plot(x_vals, y_vals, label='Interpolacion de Newton')

x_cos = np.arange(0, 5*np.pi, 0.1)
y_cos = np.cos(x_cos)

plt.plot(x_cos, y_cos, color='green', label='funcion')
plt.legend()
plt.show()

