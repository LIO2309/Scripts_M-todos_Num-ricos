import sympy as sp

def interpolacion_lineal(x0, y0, x1, y1):
    # Calculamos la pendiente (m)
    m = (y1 - y0) / (x1 - x0)
    
    # Calculamos el termino independiente (b)
    b = y0 - m * x0
    
    # Devolvemos el polinomio P(x) como una funcion lambda
    P = lambda x: m * x + b
    return P

# Puntos dados
x0, y0 = 1, 2
x1, y1 = 4, 3

# Obtenemos el polinomio de interpolacion
P = interpolacion_lineal(x0, y0, x1, y1)

# Probamos el polinomio con un valor de x
x = 2.5
y = P(x)

print(f"P({x}) = {y}")

x = sp.symbols('x')
P_simb = (y1 - y0) / (x1 - x0) * x + (x1 * y0 - x0 * y1) / (x1 - x0)
P_simb = sp.simplify(P_simb)

print(f"P(x) = {P_simb}")

def aproximar_derivada(f, a, b):
    """
    Aproxima la derivada de f en el punto a usando los valores de f(a) y f(b).
    
    Parametros:
    f: funcion, la funcion de la cual se desea aproximar la derivada
    a: float, el punto donde se quiere aproximar la derivada
    b: float, un punto cercano a a
    
    Retorna:
    float, la aproximacion de la derivada de f en a
    """
    return (f(b) - f(a)) / (b - a)

# Ejemplo de uso
# Definimos una funcion f
def f(x):
    return x**2  # Por ejemplo, f(x) = x^2

# Puntos a y b
a = 1
b = 1.1

# Calculamos la aproximacion de la derivada
derivada_aproximada = aproximar_derivada(f, a, b)
print(f"La aproximacion de la derivada de f en a={a} es {derivada_aproximada}")

def regla_trapecio(f, a, b):
    """
    Aproxima el valor de la integral definida de f en [a, b] utilizando la regla del trapecio.
    
    Parametros:
    f: funcion, la funcion a integrar
    a: float, limite inferior del intervalo de integracion
    b: float, limite superior del intervalo de integracion
    
    Retorna:
    float, la aproximacion de la integral definida de f en [a, b]
    """
    return (b - a) * (f(a) + f(b)) / 2

# Ejemplo de uso
# Definimos la funcion f
def f(x):
    return x**2  # Por ejemplo, f(x) = x^2

# Definimos los limites de integracion
a = 0.5
b = 1

# Calculamos la aproximacion de la integral definida
integral_aproximada = regla_trapecio(f, a, b)
print(f"Aproximacion de la integral definida de f en [{a}, {b}]: {integral_aproximada}")
