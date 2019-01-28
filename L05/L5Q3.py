def count_vowels(s):
    ''' Given parameter s, calculate and return 
        the number of letters 'a', 'e', 'i', 'o', 'u', 
        'A', 'E', 'I', 'O', 'U' in a given string s '''
        
    vowels = 'aeiouAEIOU'
    return sum([s.count(vowel) for vowel in vowels])

print(count_vowels('This is a test'))
