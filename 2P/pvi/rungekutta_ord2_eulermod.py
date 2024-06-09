"""
1) definir ecuacion diferencial
2) definir parametros de entrada
3) definir numero de decimales

"""


def f(t, y):
    """
    Define la funcion f(t, y) que representa la ecuacion diferencial.
    Aqui es donde defines tu ecuacion diferencial.
    """
    # Por ejemplo, vamos a resolver la ecuacion diferencial y' = t - y
    return t - y

def runge_kutta_ord2_eulermod(f, a, b, y0, M):
    """
    Implementa el metodo de Runge-Kutta de orden 2 para resolver la ecuacion diferencial.
    """
    # Calculamos h
    h = (b - a) / M

    # Inicializamos t y y
    t = a
    y = y0

    # Arrays para almacenar los valores de t e y
    t_values = [t]
    y_values = [y]

    # Iteramos para calcular yn+1 en cada paso
    for _ in range(M):
        # Calculamos k1
        k1 = h * f(t, y)

        # Calculamos k2
        k2 = h * f(t + (h * 0.5), y + (k1 * 0.5))

        # Calculamos yn+1
        y += k2

        # Actualizamos t para el proximo paso
        t += h

        # Agregamos los valores de t e y a los arreglos
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

## Parametros del problema ##
a = 0  # Punto inicial
b = 1  # Punto final
y0 = 1  # Condicion inicial
M = 100 # Numero de pasos
#############################

# Resolvemos la ecuacion diferencial
t_result, y_result = runge_kutta_ord2_eulermod(f, a, b, y0, M)

# Imprimimos los valores de t e y de manera ordenada y tabulada
for i, (t, y) in enumerate(zip(t_result, y_result)):
    print("t[{}] = {:.7f}\ty[{}] = {:.7f}".format(i, t, i, y))  # Cambiar el número para la cantidad de decimales