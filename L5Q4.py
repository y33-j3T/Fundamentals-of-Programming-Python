def vector_product3(a, b):
    ''' Given parameters a and b, calculate and return 
        a list which contains the vector product of 
        3d-vectors a and b where a=[ax, ay, az] and 
        b=[bx, by, bz] '''
        
    return [a[1] * b[2] - a[2] * b[1], 
            a[2] * b[0] - a[0] * b[2], 
            a[0] * b[1] - a[1] * b[0]]
    
print(vector_product3([1, 2, 4], [3, 5, 6]))