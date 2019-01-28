def cubic(x):
    return x**3

def square(x):
    return x**2

def sum_f(f, xs):
    ''' Given parameters f and xs, return the sum 
        of the function values of f evaluated at 
        values x0, x1, x2, ..., xn where xs=[x0,x1,x2,...,xn] '''
        
    return sum([f(x) for x in xs])

print(sum_f(square, [1, 2, 3, 10]))
print(sum_f(cubic, [1, 2, 3, 10]))