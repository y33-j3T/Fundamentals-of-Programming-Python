def interval_point(a, b, x):
    ''' Given parameters a, b, and x, take three numbers 
        and interpret a and b as the start and end point 
        of an interval, and x as a fraction between 0 and 1 
        that determines how far to go towards b, starting at a '''
        
    return (abs(a-b)*x+a)

print(interval_point(100, 200, 0.2))