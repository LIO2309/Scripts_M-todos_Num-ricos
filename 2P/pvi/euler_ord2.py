# import numpy as np
# import matplotlib.pyplot as plt

# Funcion que implementa el metodo de Euler para resolver la EDO
# def euler_method(f, x0, t0, t1, h):
#     t_values = np.arange(t0, t1 + h, h)
#     n_steps = len(t_values)
#     x_values = np.zeros((n_steps, len(x0)))
#     x_values[0] = x0
    
#     for i in range(1, n_steps):
#         x_values[i] = x_values[i - 1] + h * f(t_values[i - 1], x_values[i - 1])
    
#     return t_values, x_values

# Definimos el sistema de EDOs
# def system(t, X):
#     x1, x2 = X
#     dx1dt = x2                                  #Derivada primera
#     dx2dt = -9.2*x1 - 0.95*(x1**3) - 0.6 * x2   #aca va la ecuacion del ejercicio
#     return np.array([dx1dt, dx2dt])

# Condiciones iniciales
# x0 = np.array([0.5, 1])   #[y(x0)=0 , y'(x0)= 0] 
# t0 = 0                  #tiempo inicial 
# t1 = 0.3                #tiempo final
# h = 0.3

# Resolviendo el sistema de EDOs usando el metodo de Euler
# t_values, x_values = euler_method(system, x0, t0, t1, h)

# Mostrar resultados
# for i in range(n):
#     print(f"t = {t_values[i]:.1f}, y(t) = {y1[i]:.6f}, y'(t) = {y2[i]:.6f}")

# Graficando los resultados
# plt.plot(t_values, x_values[:, 0], label='x(t)')
# plt.plot(t_values, x_values[:, 1], label="x'(t)")
# plt.xlabel('t')
# plt.ylabel('x')
# plt.legend()
# plt.title('Solucion de la EDO usando el metodo de Euler')
# plt.grid(True)
# plt.show()


### NUEVO CODIGO ###

import math as m
import numpy as np
import matplotlib.pyplot as plt

# Método de Euler para resolver una EDO de segundo orden con PVI.
def euler_2nd_order(f, t0, y0, v0, h, n):

    # Asegurarse de que n sea un entero
    n = int(n)
    
    ts = np.zeros(n+1)
    ys = np.zeros(n+1)
    vs = np.zeros(n+1)
    
    # Condiciones iniciales
    ts[0] = t0
    ys[0] = y0
    vs[0] = v0

    # Imprimir encabezado de la tabla
    print(f"{'Paso':^5} {'t':^10} {'y':^10} {'v (dy/dt)':^15}")
    print("-" * 45)
    print(f"{0:^5} {ts[0]:^10.6f} {ys[0]:^10.6f} {vs[0]:^15.6f}")
    
    # Método de Euler
    for i in range(1, n+1):
        ys[i] = ys[i-1] + h * vs[i-1]  # Actualizamos y usando dy/dt = v
        vs[i] = vs[i-1] + h * f(ts[i-1], ys[i-1], vs[i-1])  # Actualizamos v usando dv/dx = f(t, y, v)
        ts[i] = ts[i-1] + h  # Incrementamos t

        # Imprimir cada fila de la tabla
        print(f"{i:^5} {ts[i]:^10.6f} {ys[i]:^10.6f} {vs[i]:^15.6f}")
    
    return ts, ys, vs

# Definimos la función que describe la EDO de segundo orden
def f(t, y, v):
    return (-5*(v) - 6*(y) + 10*m.sin(t))

# Parámetros del problema
t0 = 0     # valor inicial de t
y0 = 0     # valor inicial de y (PVI: y(0) = 0)
v0 = 5     # valor inicial de dy/dt (PVI: dy/dt(0) = 5)
h = 0.1    # tamaño de paso
n = 3/h      # número de pasos siendo 3 el valor que piden de t

# Ejecutar el método de Euler para EDO de segundo orden
ts, ys, vs = euler_2nd_order(f, t0, y0, v0, h, n)

# Graficar los resultados
plt.plot(ts, ys, label='y (Solución)')
plt.plot(ts, vs, label="v = dy/dt")
plt.xlabel('t')
plt.ylabel('y, dy/dt')
plt.title('Solución aproximada usando el método de Euler para una EDO de segundo orden')
plt.legend()
plt.grid(True)
plt.show()