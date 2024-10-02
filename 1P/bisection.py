# Para estos ejercicios tengo que reemplazar directamente los valores que me pide


import math as m

def p(x):
    return (x**2 - m.sin(x) - 0.5)     #editar funcion


def bisect(a, b, f, error):         # a = inicio, b = fin, f = funcion, error = el minimo que quiero
    left = a
    right = b
    med = (b + a) / 2  # Esta es mi primer aproximacion
    err = (b - a) / 2
    steps = 0

    while (err > error):
        if f(a) * f(med) < 0:
            b = med
        else:
            a = med
        med = (a + b) / 2
        err = (b - a) / 2
        steps += 1

    return (med, err, steps)


ans = bisect(0, 2, p, 10**(-3)) #ext izq, ext der, func, err al que debe ser menor

print(f'Solucion: {ans[0]}\nError: {ans[1]}\nPasos: {ans[2]}')
