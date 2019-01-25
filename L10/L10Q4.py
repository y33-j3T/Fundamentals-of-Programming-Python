import numpy as np
from scipy.optimize import curve_fit 
from scipy.optimize import brentq

def model(t, Ti, Ta, c):
    ''' Given parameters t, Ti, Ta and c, where
        t: time passed in seconds
        Ti: initial temperature in degree Celsius,
        Ta: ambient temperature in degree Celsius,
        c: time constant for the cooling process in seconds.
        
        Return a model equation to obtain temperature T
        at time t '''
        
    return (Ti-Ta)*np.exp((-t)/c) + Ta

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

def extract_parameters(ts, Ts):
    ''' Given parameters ts and Ts, 
        expect a numpy array ts with time values and 
        a numpy array Ts of the same length as ts 
        with corresponding temperature values.
        
        The function should estimate and return a tuple 
        of the three model parameters Ti, Ta and c (in this order) 
        by fitting the model function as in equation (1) to 
        the data ts and Ts '''
        
    params, extras = curve_fit(model, ts, Ts, p0=(100, 0, 10))
    return params

def sixty_degree_time(Ti, Ta, c):
    """ Given parameters Ti, Ta and c, where
        Ti: initial temperature 
        Ta: ambient temperature
        c: cooling rate time constant
        
        Return an estimate of the number of seconds after 
        which the temperature of the drink has cooled down 
        to 60 degree Celsius """
        
    f = lambda t: model(t, Ti, Ta, c) - 60
    ans = brentq(f, 0, 10000)
    return ans

datats, dataTs = read2coldata('temperature-data.txt')
fTi, fTa, fc = extract_parameters(datats, dataTs)
print("Best fit initial temperature: ", fTi)
print("Best fit ambient temperature: ", fTa)
print("Best fit time constant: ", fc)
print("")
# What was the initial temperature of the tea in the cup at time t=0s?
Q1ans = model(0, fTi, fTa, fc)
print("Initial temperature of tea at time t=0s: ", Q1ans)

# How quickly does the tea cool down? 
# In particular: after what time is it safe to drink it?
# (we assume that 60C is a safe temperature)
Q2ans =  sixty_degree_time(fTi, fTa, fc)
print("Time needed to reach 60C from initial temperature: ", Q2ans, "seconds")

#What will be the final temperature of the tea if we wait infinitely long? 
#(presumably this will be the room temperature in this particular lab in Java)
Q3ans = model(100000000000, fTi, fTa, fc)
print("Final temperature: ", Q3ans)
        