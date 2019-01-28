def box_volume(a=13, b=11, c=2):
    ''' Given parameters a, b and c, calculate and
        return the volume of a box with edge lengths 
        a, b and c in inch^3.
        
        The standard dimensions of the UPS express box (small) 
        are a=13 inch, b=11 inch and c=2 inch.

        The function will use these values for a, b and c unless 
        others are provided '''
        
    return a*b*c

print(box_volume())
print(box_volume(3, 4, 5))
print(box_volume(a=2, b=3))

