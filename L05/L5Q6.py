def seq_mult_scalar(a, s):
    ''' Given parameters a and s, for input 
         a=[a0, a1, a2,.., an], return 
         [s * a0, s * a1, s * a2, ..., s * an] '''
     
    return [s*num for num in a]
 
print(seq_mult_scalar([-4, 9, 1], 10))