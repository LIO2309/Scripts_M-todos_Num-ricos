import numpy as np
import matplotlib.pyplot as plt
import math as m

def f(t, y): #Esta es la EDO
    return (t - y)/2 

def y_real(t):
    return 3* m.exp(-t/2) + t - 2

def euler_method(f, a, b, M, xin):
    
    # Implementa el metodo de Eueler
    # :Problema:
    # y' = f(t,y)
    # y(a) = xin    (el valor inicial)
    ts = []
    ys = []
    ans=[]

    h = (b - a) / float(M)

    t = a
    y = xin

    ts.append(a)
    ys.append(xin)
    ans.append((a,xin))

    for step in range(M):
        y += h * f(t, y)
        t += h
        ts.append(t)
        ys.append(y) 
        ans.append((t,y))

    for i in range(n):
        t.append(t[i] + h)
        y.append(round(y[i] + h* f(t[i], y[i]), 3))
        error.append(abs(ys(ts[i])- ys[i]))
        
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.scatter(t, y)
    plt.plot(t, y, c="green")

    x = np.linspace(a, b, 100)
    y_r = [y_real(i) for i in x] 

    plt.plot(x, y_r, c="red")
        
        
    return ts, ys, ans

ts, ys, ans = euler_method(f, 0, 3, 6,1 )

#print(ys)
#print(ts)
print("(t_k, y_k):")
for i in range(len(ans)):
    print(f'k={i}: {ans[i]}')
    
    