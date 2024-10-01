# Pasos: 
#   1. definir ecuacion diferencial
#   2. definir parametros de entrada
#   3. definir numero de decimales

import math as m

def f(t, y):

    return (-(y)**2)        #ecuacion diferencial en funcion de y' 


# Implementa el metodo de Runge-Kutta de orden 2 para resolver la ecuacion diferencial
def runge_kutta_ord2_heun(f, a, b, y0, M):

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
        k2 = h * f(t + h, y + k1)


        # Calculamos yn+1 

        # Si es Heun
        y += (1/2) * (k1 + k2)
        
        # Si es Ralston
        # y += ((1/3)*k1) + ((2/3)*k2)  


        # Actualizamos t para el proximo paso
        t += h

        # Agregamos los valores de t e y a los arreglos
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

## Parametros del problema ##
a = 0  # Punto inicial
b = 0.1  # Punto final
y0 = 1  # Condicion inicial
M = 5 # Numero de pasos
#############################

# Resolvemos la ecuacion diferencial
t_result, y_result = runge_kutta_ord2_heun(f, a, b, y0, M)

# Imprimimos los valores de t e y de manera ordenada y tabulada
for i, (t, y) in enumerate(zip(t_result, y_result)):
    print("t[{}] = {:.7f}\ty[{}] = {:.7f}".format(i, t, i, y))  # Cambiar el número para la cantidad de decimales