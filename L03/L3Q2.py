def min_max(xs):
    ''' Given parameter xs, compute the minimum 
        value xmin of the elements in the list xs, 
        and the maximum value xmax of the elements 
        in the list, and returns a tuple (xmin,xmax) '''
    
    return min(xs), max(xs)

print(min_max([0, 1, 2, 10, -5, 3]))