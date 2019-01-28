def is_palindrome(s):
    ''' Given parameter s, return the value True if s 
        is a palindrome, and returns False otherwise '''
        
    if s==s[::-1]:
        return True
    else:
        return False
    
print(is_palindrome('rotator'))
print(is_palindrome('radiator'))
print(is_palindrome('ABBA'))