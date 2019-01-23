import math

def f(x):
    return x**2-2

def g(x):
    return math.sin(x) + 1.1 # has no root!

def fprime(x):
    ''' Given parameter x, approximate the first derivative 
        (df(x)/dx) at position x '''
    eps = 1e-6
    return (f(x + eps/2) - f(x - eps/2))/eps

def newton(f, x, feps, maxit):
    ''' Given parameters f, x, feps and maxit, 
        take a function f(x) and an initial guess x 
        for the root of the function f(x), 
        an allowed tolerance feps and the maximum number 
        of iterations that are allowed maxit.
        
        If more than maxit iterations are necessary for 
        the function newton, then the newton function should 
        raise the RuntimeError exception with the message: 
        Failed after X iterations where X is to be replaced with 
        the number of iterations'''
        
    maxit_copy = maxit
    while abs(f(x)) > feps:
        if maxit_copy > 0:
            x = x - f(x) / fprime(x)
            maxit_copy-=1
        else:
            raise RuntimeError("Failed after %d iterations" % maxit)
    
    return x

print(newton(f, 1.0, 0.2, 15))
print(newton(f, 1.0, 0.2, 15) - math.sqrt(2))
print(newton(f, 1.0, 0.001, 15))
print(newton(f, 1.0, 0.001, 15) - math.sqrt(2))
print(newton(f, 1.0, 0.000001, 15) - math.sqrt(2))
print(newton(g, 1.0, 0.02, 15))
