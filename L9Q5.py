from scipy.integrate import quad

def using_quad():
    ''' Compute the integral of x^2 from a=-1 to b=2 
        using function quad from scipy.integrate.
        
         The function using_quad should return the value 
         that the quad() function returns, 
         i.e. a tuple (y, abserr) where 
         y is quad's best approximation of the true integral, 
         and abserr an absolute error estimate ''' 
         
    y, abserr = quad(lambda x: x*x, -1, 2)
    return y, abserr

print(using_quad())