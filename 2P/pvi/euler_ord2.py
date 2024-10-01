import numpy as np
import matplotlib.pyplot as plt

# Funcion que implementa el metodo de Euler para resolver la EDO
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
    dx1dt = x2                                  #Derivada primera
    dx2dt = -9.2*x1 - 0.95*(x1**3) - 0.6 * x2   #aca va la ecuacion del ejercicio
    return np.array([dx1dt, dx2dt])

# Condiciones iniciales
x0 = np.array([0.5, 1])   #[y(x0)=0 , y'(x0)= 0] 
t0 = 0                  #tiempo inicial 
t1 = 0.3                #tiempo final
h = 0.3

# Resolviendo el sistema de EDOs usando el metodo de Euler
t_values, x_values = euler_method(system, x0, t0, t1, h)

# Mostrar resultados
for i in range(n):
    print(f"t = {t_values[i]:.1f}, y(t) = {y1[i]:.6f}, y'(t) = {y2[i]:.6f}")

# Graficando los resultados
plt.plot(t_values, x_values[:, 0], label='x(t)')
plt.plot(t_values, x_values[:, 1], label="x'(t)")
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title('Solucion de la EDO usando el metodo de Euler')
plt.grid(True)
plt.show()