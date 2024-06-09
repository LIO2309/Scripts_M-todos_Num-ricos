import math as m

# m.cos() , m.exp()

def p(x):   #f
    #return x**2 * m.log(x) - x - 10
    return m.exp(x) - m.sin(x)
    
def dp(x):  #f'
    #return 2*x * m.log(x) + (1/x)*(x**2)-1
    return m.exp(x) - m.cos(x)

def newton(init, f, df, error):
    x=init
    y=x-(f(x)/df(x))
    err=abs(y-x)
    steps = 1

    while(abs(y-x)>error):
        x=y
        y=x-(f(x)/df(x))
        steps +=1
        err=abs(y-x)
    return (y, steps, err)

ans = newton(-3,p,dp,0.001)

print(f'La raiz esta en {ans[0]}. Se encontro con {ans[1]} pasos. Tiene un error de {ans[2]}')

#check q f'(x)!=0 para [a,b]