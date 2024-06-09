import numpy as np

def runge_kutta_4(f, a, b, y0, N):
    # Definir el paso
    h = (b - a) / N
    
    # Crear los puntos t_k
    t = np.linspace(a, b, N+1)
    
    # Inicializar y con la condición inicial
    y = np.zeros(N+1)
    y[0] = y0
    
    # Iterar para calcular y_k usando el método de Runge-Kutta de orden 4
    for k in range(N):
        tk = t[k]
        yk = y[k]
        
        k1 = h * f(tk, yk)
        k2 = h * f(tk + h/2, yk + k1/2)
        k3 = h * f(tk + h/2, yk + k2/2)
        k4 = h * f(tk + h, yk + k3)
        
        y[k+1] = yk + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    return t, y

# Ejemplo de uso con una ecuación diferencial específica
# y' = f(t, y) = t - y
def f(t, y):
    return t - y

# Parámetros
a = 0   # límite inferior
b = 1   # límite superior
y0 = 1  # condición inicial
N = 100  # número de intervalos

# Ejecutar el método de Runge-Kutta de orden 4
t, y = runge_kutta_4(f, a, b, y0, N)

# Imprimir los resultados
for i in range(len(t)):
    print(f"t[{i}] = {t[i]:.7f}, y[{i}] = {y[i]:.7f}")
