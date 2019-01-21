def count_sub_in_file(filename, s):
    ''' Given parameters filename and s, calculate and
        return the number of occurrences of s in the 
        file given through filename '''
        
    file = open(filename, 'r')
    return file.read().split().count(s)
    file.close()
    
print(count_sub_in_file('data.txt', 'Alice'))