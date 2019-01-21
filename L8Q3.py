def cubic(x):
    return x**3

def square(x):
    return x*x
    
def make_filter(f):
    ''' Given parameter f, make a filter for 
        function f '''
        
    def larger_than_zero(x):
        if f(x)>0:
            return True
        else:
            return False
    return larger_than_zero
    
def positive_places(f, xs):
    ''' Given parameters f and list_of_num, 
        returns a list of those-and-only-those 
        elements x of xs for which f(x) is 
        strictly greater than zero '''
    
    positive_nums = filter(make_filter(f), xs)
    return list(positive_nums)
        
print(positive_places(cubic, [1, 2, -3, 4, -5]))
print(positive_places(square, [1, 2, -3, 4, -5]))
