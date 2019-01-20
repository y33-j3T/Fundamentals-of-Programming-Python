def box_surface(a, b, c):
    ''' Given parameters a, b and c, calculate and
        return the surface area of a box (i.e. cuboid) 
        with these edge lengths a, b, c '''
        
    return (2*a*b + 2*b*c + 2*a*c)

print(box_surface(2, 2, 0))