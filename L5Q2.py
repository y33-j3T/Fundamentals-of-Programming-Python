def count_sub_in_file(filename, s):
    ''' Given parameters filename and s, calculate and
        return the number of occurrences of s in the 
        file given through filename '''
        
    file = open(filename, 'r')
    count = file.read().split().count(s)
    if(count>0):
        return count
    else:
        return -1
    file.close()
    
print(count_sub_in_file('data.txt', 'Alice'))