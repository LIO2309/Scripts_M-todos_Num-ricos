import math

# Función para la segunda derivada y''(t)
def y_double_prime(t, y, y_prime):
    # Aquí debes definir la expresión de y''(t)
    # Por ejemplo, vamos a resolver la ecuación y''(t) = -y - 2y'
    return -0.5*y + 5

# Método de Taylor de segundo orden para una EDO de segundo orden
def taylor_segundo_orden(edo_y_double_prime, t0, y0, y_prime0, h, num_pasos):
    # Inicializar las listas para almacenar t, y y'
    t_values = []
    y_values = []
    y_prime_values = []

    # Agregar los valores iniciales
    t = t0
    y = y0
    y_prime = y_prime0

    # Iterar sobre el número de pasos
    for _ in range(num_pasos):
        # Guardar los valores actuales de t, y, y'
        t_values.append(t)
        y_values.append(y)
        y_prime_values.append(y_prime)

        # Calcular y''(t) usando la función proporcionada
        y_double_prime_val = edo_y_double_prime(t, y, y_prime)

        # Calcular y(t+h) y y'(t+h) usando el método de Taylor de segundo orden
        y_next = y + h * y_prime + (h**2 / 2) * y_double_prime_val
        y_prime_next = y_prime + h * y_double_prime_val

        # Actualizar t y y' para el siguiente paso
        t += h
        y = y_next
        y_prime = y_prime_next

    return t_values, y_values, y_prime_values

# Función principal para resolver la EDO y''(t) = -y - 2y'
def resolver_edo_segundo_orden(y_double_prime_func, t0, y0, y_prime0, h, num_pasos):
    # Llamar al método de Taylor de segundo orden
    t_values, y_values, y_prime_values = taylor_segundo_orden(y_double_prime_func, t0, y0, y_prime0, h, num_pasos)

    # Imprimir los resultados en orden t, y, y'
    print("t\ty\ty'")
    for i in range(len(t_values)):
        print(f"{t_values[i]}\t{y_values[i]}\t{y_prime_values[i]}")

# Ejemplo de uso
if __name__ == "__main__":
    # Definir los parámetros iniciales
    t0 = 0
    y0 = 0  # Valor inicial de y(t0)
    y_prime0 = 0  # Valor inicial de y'(t0)
    h = 0.1  # Tamaño del paso
    num_pasos = 12  # Número de pasos a calcular

    # Resolver la EDO 
    resolver_edo_segundo_orden(y_double_prime, t0, y0, y_prime0, h, num_pasos)
