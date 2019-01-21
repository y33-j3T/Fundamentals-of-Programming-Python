def count_chars(s):
    ''' Given parameter s, take a string s and return 
        a dictionary. The dictionary's keys are the set of 
        characters that occur in string s. The value for 
        each key is the number of times that this character 
        occurs in the string s '''
    
    my_str = list(s)
    char_count={}
    for char in my_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count
        
print(count_chars("abcdeABCDE"))
    
    
    
    