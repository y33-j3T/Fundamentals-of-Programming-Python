import numpy as np
from scipy.optimize import curve_fit 
import pylab

def model(t, Ti, Ta, c):
    ''' Given parameters t, Ti, Ta and c, where
        t is the time passed in seconds
        Ti is the initial temperature in degree Celsius,
        Ta is the ambient temperature in degree Celsius,
        c is the time constant for the cooling process in seconds.
        return a model equation to obtain temperature T
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
        
def plot(ts, Ts, Ti, Ta, c):
    """ Input Parameters:

        ts : Data for time (ts)
                (numpy array)
        Ts : data for temperature (Ts)
                (numpy arrays)
        Ti : model parameter Ti for Initial Temperature
                (number)
        Ta : model parameter Ta for Ambient Temperature
                (number)
        c  : model parameter c for the time constant
                (number)

        This function will create plot that shows the model fit together
        with the data.

        Function returns None. """
        
    pylab.plot(ts, Ts, 'o', label='data')
    params = extract_parameters(ts, Ts)
    fTs = model(ts, params[0], params[1], params[2])
    pylab.plot(ts, fTs, 'r-', label='fitted')
    pylab.legend()
    pylab.show()
     
        
datats, dataTs = read2coldata('temperature-data.txt')
plot(datats, dataTs, 100, 0, 10)

