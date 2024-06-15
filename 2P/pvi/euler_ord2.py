import numpy as np
import matplotlib.pyplot as plt

# Función que implementa el método de Euler para resolver la EDO
def euler_method(f, x0, t0, t1, h):
    t_values = np.arange(t0, t1 + h, h)
    n_steps = len(t_values)
    x_values = np.zeros((n_steps, len(x0)))
    x_values[0] = x0
    
    for i in range(1, n_steps):
        x_values[i] = x_values[i - 1] + h * f(t_values[i - 1], x_values[i - 1])
    
    return t_values, x_values

# Definimos el sistema de EDOs
def system(t, X):
    x1, x2 = X
    dx1dt = x2
    dx2dt = -x1
    return np.array([dx1dt, dx2dt])

# Condiciones iniciales
x0 = np.array([0, 1])   
t0 = 0                  #tiempo inicial 
t1 = 1                  #tiempo final
h = 0.1

# Resolviendo el sistema de EDOs usando el método de Euler
t_values, x_values = euler_method(system, x0, t0, t1, h)

# Graficando los resultados
plt.plot(t_values, x_values[:, 0], label='x(t)')
plt.plot(t_values, x_values[:, 1], label="x'(t)")
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title('Solución de la EDO usando el método de Euler')
plt.grid(True)
plt.show()