def reverse_dic(d):
    ''' Given parameter d, take a dictionary d 
        as the input argument and returns a 
        dictionary r. 
        
        If the dictionary d has a key k and an 
        associated value v, then the dictionary r 
        should have a key v and a value k '''
        
    reversed_dic = {v:k for k, v in d.items()}
    return reversed_dic

some_dic = {'A': "MGLOLZ",
            'B': "MGLULZ",
            'C': "OMGOMG"}

print(reverse_dic(some_dic))