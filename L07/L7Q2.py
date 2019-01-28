def square(x):
    return x*x

def deriative(f, x):
    ''' Given parameters f and x, compute a numerical 
        approximation of the first derivative of the 
        function f(x) using central differences '''
        
    eps = 1e-6
    return (f(x + eps/2) - f(x - eps/2))/eps

print(deriative(square, 0))
print(deriative(square, 1))
print(deriative(square, 2))