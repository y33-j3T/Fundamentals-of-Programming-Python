def count(element, seq):
    ''' Given parameters element and seq,  
        counts how often the given element, element 
        occurs in the given sequence, seq 
        and returns this integer value '''
        
    return seq.count(element)

print(count('a', ['a', 'b', 'c', 'a']))