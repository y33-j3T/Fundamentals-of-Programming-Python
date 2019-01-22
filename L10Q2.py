import numpy as np

def read2coldata(filename):
    ''' Open a text file with two columns of data. 
        The columns have to be separated by white space.
        Return a tuple of two numpy-arrays where the 
        first contains all the data from the first column in the file, 
        and the second all the data in the second column '''
    
    data = np.loadtxt(fname = filename)
    arr1 = data[:, 0]
    arr2 = data[:, 1]
    return arr1, arr2
    
print(read2coldata('testdata.txt'))