import math as m

def punto_fijo(funcion, x_0, tolerancia, max_pasos):
    x_1=funcion(x_0)
    secuencia = [x_0, x_1]
    n=0
    while abs(x_1-x_0) > tolerancia and n<max_pasos:
        n=n+1
        x_0 = x_1
        x_1 = funcion(x_0)
        secuencia.append(x_1)
    if n==max_pasos:
        print('Termino por la cantidad de pasos')
    else:
        print('Llego a la tolerancia (error)')
    return (secuencia,x_1,n, x_1-x_0)

def f(x):
    #return m.pow(x+1, 1/3) # la raiz cubica
    return m.exp(-x)

#print(punto_fijo(f, 1, 0.00001,20)[0]) #imprime la secuencia


ans = punto_fijo(f, 0.5, 0.01,20)  # el valor inicial es uno entre dos numeros
                                    #cuyas imagenes son de signos distintos


print(f'Raiz = {ans[1]}\nPasos = {ans[2]}\nError = {ans[3]}')


