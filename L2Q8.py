import math

def triangle_area(a, b, c):
    ''' Given parameters a, b and c, calculate and
        return the area A of a triangle with 
        edge lengths a, b, c '''
        
    s = (a+b+c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

print(triangle_area(3, 4, 5))