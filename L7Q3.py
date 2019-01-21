import math

def square(x):
    return x*x

def deriative(f, x, eps=1e-6):
    ''' Given parameters f, x and eps, compute a numerical 
        approximation of the first derivative of the 
        function f(x) using central differences '''
        
    return (f(x + eps/2) - f(x - eps/2))/eps

print(deriative(math.exp, 0, 0.1))
print(deriative(math.exp, 0))
print(deriative(math.exp, 0, eps=1e-6))
