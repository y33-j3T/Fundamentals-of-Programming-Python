import math

def degree(x):
    ''' Given parameter x, take x in radian 
        and return the corresponding value 
        in degrees '''
        
    return (360*x)/(2*math.pi)

print(degree())