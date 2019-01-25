def geometric_mean(xs):
    ''' Given parameter xs, compute the 
        geometric mean of the numbers given 
        in the list xs '''
        
    result=1
    for num in xs:
        result*=num
        
    return result**(1/len(xs))

print(geometric_mean([1, 2]))