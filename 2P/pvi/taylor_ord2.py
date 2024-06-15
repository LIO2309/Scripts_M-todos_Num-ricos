import numpy as np
import matplotlib.pyplot as plt

def taylor_order2(f, dfdt, dfdx, x0, y0, h, n):
    """
    Método de Taylor de segundo orden para resolver EDOs.
    
    Parámetros:
    f    : función f(t, y) que define la EDO dy/dt = f(t, y)
    dfdt : derivada parcial de f con respecto a t
    dfdx : derivada parcial de f con respecto a y
    x0   : valor inicial de t
    y0   : valor inicial de y
    h    : paso de integración
    n    : número de pasos
    
    Retorna:
    t_values : array con los valores de t
    y_values : array con los valores de y
    """
    
    # Inicializar los arrays para t y y
    t_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    
    # Asignar valores iniciales
    t_values[0] = x0
    y_values[0] = y0
    
    # Iterar usando el método de Taylor de segundo orden
    for i in range(n):
        t = t_values[i]
        y = y_values[i]
        
        f_val = f(t, y)
        dfdt_val = dfdt(t, y)
        dfdx_val = dfdx(t, y)
        
        y_values[i+1] = y + h * f_val + (h**2 / 2) * (dfdt_val + f_val * dfdx_val)
        t_values[i+1] = t + h
    
    return t_values, y_values

# Definir la función f(t, y), df/dt y df/dy
def f(t, y):
    return -2 * t * y

def dfdt(t, y):
    return -2 * y

def dfdx(t, y):
    return -2 * t

# Parámetros iniciales
x0 = 0
y0 = 1
h = 0.1
n = 20

# Obtener los resultados
t_values, y_values = taylor_order2(f, dfdt, dfdx, x0, y0, h, n)

# Graficar los resultados
plt.plot(t_values, y_values, 'o-', label='Aproximación de Taylor (orden 2)')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Solución usando el método de Taylor de segundo orden')
plt.grid(True)
plt.show()
