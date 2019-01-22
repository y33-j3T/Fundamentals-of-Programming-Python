from scipy.integrate import quad

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

def finderror(n):
    ''' Use the trapez() function to find the error of 
        the trapezoidal integral approximation.
        
        The function should compute the integral of 
        f(x) = x*x with integration limits a = -1 and 
        b = 2 numerically. 
        
        The function should then subtract this numerical 
        result A from the exact integral value I and 
        return the difference '''
        
    I_trapezium = trapez(square, -1, 2, n)
    I_quad, err = quad(square, -1, 2)
    return I_quad - I_trapezium
    
print(finderror(5))
    