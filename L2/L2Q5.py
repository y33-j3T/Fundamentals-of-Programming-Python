def signum(x):
    ''' Given parameter x, 
        return 1 if x > 0,
        return 0 if x = 0,
        return -1 if x < 0 '''
        
    if(x>0):
        return 1
    elif(x==0):
        return 0
    else:
        return -1
    
print(signum(2012))