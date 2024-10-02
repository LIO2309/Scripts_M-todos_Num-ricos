import math as m
import numpy as np
import matplotlib.pyplot as plt

# Método de Euler para resolver una EDO de orden 1 con PVI.
def euler(f, t0, y0, h, n):

    # Asegurarse de que n sea un entero
    n = int(n)

    ts = np.zeros(n+1)
    ys = np.zeros(n+1)
    
    ts[0] = t0
    ys[0] = y0
    
    # Imprimir encabezado de la tabla
    print(f"{'Paso':^5} {'t':^10} {'y':^10}")
    print("-" * 25)
    print(f"{0:^5} {ts[0]:^10.6f} {ys[0]:^10.6f}")
    
    for i in range(1, n+1):
        ys[i] = ys[i-1] + h * f(ts[i-1], ys[i-1])
        ts[i] = ts[i-1] + h
        
        # Imprimir cada fila de la tabla
        print(f"{i:^5} {ts[i]:^10.6f} {ys[i]:^10.6f}")
    
    return ts, ys

# Definimos la función que describe la EDO
def f(t, y):
    return ((y) - 0.5*m.exp((t)/2)*m.sin(5*(t)) + 5*m.exp((t)/2)*m.cos(5*(t)))

# Parámetros
t0 = 0          # valor inicial de t
y0 = 0          # valor inicial de y (PVI: y(0) = 0)
a = 0           # extremo izq del intervalo
b = 1           # extremo der del intervalo
h = 0.1         # tamaño de paso
n = (b-a)/h     # número de pasos (debe ser entero)

# Ejecutar el método de Euler
ts, ys = euler(f, t0, y0, h, n)

# Graficar los resultados
plt.plot(ts, ys, label='Aproximación Euler')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solución aproximada usando el método de Euler')
plt.legend()
plt.grid(True)
plt.show()