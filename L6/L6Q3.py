def cubic(x):
    return x**3

def square(x):
    return x**2

def eval_f(f, xs):
    ''' Given parameters f and xs, apply the function 
        f subsequently to every value x in xs
        and return a list fs of function values '''
    return [f(x) for x in xs] 

print(eval_f(cubic, [-1, 10, 20, 42]))
print(eval_f(square, [-1, 10, 20, 42]))

import math
print(eval_f(math.sqrt, [1, 10, 20, 42]))