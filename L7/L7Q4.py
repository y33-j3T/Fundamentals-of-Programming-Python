import math

def f(x):
    return x**2-2

def fprime(x):
    ''' Given parameter x, approximate the first derivative 
        (df(x)/dx) at position x '''
    eps = 1e-6
    return (f(x + eps/2) - f(x - eps/2))/eps

def newton(f, x, feps, maxit):
    ''' Given parameters f, x, feps and maxit, 
        take a function f(x) and an initial guess x 
        for the root of the function f(x), 
        an allowed tolerance feps and 
        the maximum number of iterations that are allowed maxit '''
        
    while abs(f(x)) > feps:
        if maxit > 0:
            x = x - f(x) / fprime(x)
            maxit-=1
        
    return x

print(newton(f, 1.0, 0.2, 15))
print(newton(f, 1.0, 0.2, 15) - math.sqrt(2))
print(newton(f, 1.0, 0.001, 15))
print(newton(f, 1.0, 0.001, 15) - math.sqrt(2))
print(newton(f, 1.0, 0.000001, 15) - math.sqrt(2))