# Básicamente en estos ejercicios me van a dar una función que dependa de x

# Primero hay que igualar la función a 0 y graficarla en geogebra para ver entre qué valores estará la raíz 
# de esa función. Luego, se necesita la ecuación explícita de  x (hay que despejar x y colocarla en el código). 

# Hay dos tipos de ejercicios:
#   1. Piden hallar la raíz
#   2. Piden calcular un cociente entre el error del último paso y el error del paso anteultimo


import math as m

def punto_fijo(funcion, x_0, tolerancia, max_pasos):
    x_1 = funcion(x_0)
    secuencia = [x_0, x_1]
    n = 0
    errores = [abs(x_1 - x_0)]
    
    while (abs(x_1 - x_0) > tolerancia) and (n < max_pasos):
        n = n + 1
        x_0 = x_1
        x_1 = funcion(x_0)
        error_nuevo = abs(x_1 - x_0)
        errores.append(error_nuevo)
        secuencia.append(x_1)

    # Calcula el cociente al final
    if len(errores) > 1:
        cociente = errores[-1] / errores[-2]  # Cociente de los dos últimos errores
    else:
        cociente = None  # Si no hay suficientes errores, el cociente es indefinido

    if n==max_pasos:
        print('Termino por la cantidad de pasos')
    else:
        print('Llego a la tolerancia (error)')
    return (secuencia,x_1,n, x_1-x_0, cociente)

def f(x):
    return (m.sqrt(10 / (4+(x)) ))    # Escribo la expresion al despejar x


ans = punto_fijo(f, 2, 10**(-9), 100)  #x_0 es el valor entero mas cercano a la raiz

print(f'Raiz = {ans[1]}\nPasos = {ans[2]}\nError = {ans[3]}\nCociente = {ans[4]}')