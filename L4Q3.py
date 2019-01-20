import math

def seq_sqrt(xs):
    ''' Given parameter xs, take a list of numbers 
        and returns a list of the same length 
        that contains the square root for 
        each number in the list '''
        
    sqrt_num=[math.sqrt(x) for x in xs]
    return sqrt_num

print(seq_sqrt([1, 2, 3, 4, 5]))
