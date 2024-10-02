
import math as m

# Define la función f(t, y) que representa la ecuación diferencial
def f(t, y):
    return ((y) - 0.5*m.exp((t)/2)*m.sin(5*(t)) + 5*m.exp((t)/2)*m.cos(5*(t)))


# Calcula la derivada de f(t, y)
def f_prime(t, y):
    
    # Calculamos la derivada parcial de f respecto a t
    df_dt = -(25.25)*m.exp((t)/2)*m.sin(5*(t))

    # Calculamos la derivada parcial de f respecto a y
    df_dy = 1

    # Devolvemos la derivada de f
    return df_dt + df_dy * f(t, y)


# Implementa el método de Taylor de orden 2 para resolver la ecuación diferencial
def taylor_2(f, f_prime, a, b, y0, M):
    
    # Calculamos h
    h = (b - a) / M

    # Inicializamos t y y
    t = a
    y = y0

    # Iteramos para calcular yk+1 en cada paso
    for _ in range(M):
        # Calculamos f(tk, yk)
        f_tk_yk = f(t, y)

        # Calculamos f'(tk, yk)
        f_prime_tk_yk = f_prime(t, y)

        # Calculamos yk+1
        y += h * f_tk_yk + (h ** 2 / 2) * f_prime_tk_yk

        # Actualizamos t para el próximo paso
        t += h

    return y

# Parámetros del problema
a = 0           # Punto inicial
b = 1           # Punto final
y0 = 0          # Condición inicial
M = 10          # Número de pasos

# Resolvemos la ecuación diferencial
resultado = taylor_2(f, f_prime, a, b, y0, M)
print("El resultado de la ecuación diferencial en t =", b, "es y =", resultado)
print("y(",b,") =", resultado)
