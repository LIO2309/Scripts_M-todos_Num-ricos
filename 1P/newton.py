# A partir de la ecuacion que te dan, se necesita: 
#   1. La derivada
#   2. El punto cercano a la raiz

# Si ingreso la ecuacion en Wolfram, me da todo lo que necesito #

# Hay como que dos tipos de ejercicios:
#   1. los que te dan de una la función y los parámetros entonces ingresas los valores directo
#   2. te dan como que una ecuación más “rebuscada” que despejas un toque e ingresas los valores


import math as m

def p(x):   #f
    return ((x)**3 + 2.967*(x)**2 - 9.46693*(x) - 11.557935)       #editar funcion
    

def dp(x):  #f'
    return (3*(x)**2 + 5.934*(x) - 9.46693)      #editar funcion derivada


def newton(init, f, df, error):
    x = init
    y = x-(f(x)/df(x))
    err = abs(y-x)
    steps = 1

    while(abs(y-x)>error):
        
        x = y
        y = x - (f(x)/df(x))
        steps += 1
        err = abs(y-x)

    return (y, steps, err)

# Respuesta (verificar que f'(x) != 0 en el [a,b])
# init es:
#   I. a si f(a) tiene el mismo signo que f''(a) 
#   II. b si f(b) tiene el mismo signo que f''(b)

ans = newton(3, p, dp, 10**(-11))   

print(f'Solucion: {ans[0]}\nPasos: {ans[1]}\nError: {ans[2]}')