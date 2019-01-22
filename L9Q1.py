def square(x):
    return x*x

def trapez(f, a, b, n):
    ''' Given parameters f, a, b and n, implement 
        the Trapezium rule to estimate integral of
        function f, from x=a to x=b with n number
        of subdivisions '''
        
    h = (b-a)/n
    x = [a+i*h for i in range(1, n)]
    fx = [f(val) for val in x]
    A = (h/2)*(f(a)+f(b)+2*sum(fx))
    return A

print(trapez(square, 0, 2, 4))
