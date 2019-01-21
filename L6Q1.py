def f(x):
    return x**3

def positive_places(f, xs):
    ''' Given parameters f and list_of_num, 
        returns a list of those-and-only-those 
        elements x of xs for which f(x) is 
        strictly greater than zero '''
        
    return [x for x in xs if f(x)>0]

print(positive_places(f, [1, 2, -3, 4, -5]))
    