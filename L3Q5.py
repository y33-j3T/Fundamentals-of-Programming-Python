def range_squared(n):
    ''' Given parameter n, take an non-negative 
        integer value n and return the list 
        [0, 1, 4, 9, 16, 25, ..., (n-1)^2]. 
        If n is zero, the function should return 
        the empty list. '''
        
    result = [x**2 for x in range(n)]
    
    return result

print(range_squared(3))
        