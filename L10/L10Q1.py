import numpy as np

def model(t, Ti, Ta, c):
    ''' Given parameters t, Ti, Ta and c, where
        t is the time passed in seconds
        Ti is the initial temperature in degree Celsius,
        Ta is the ambient temperature in degree Celsius,
        c is the time constant for the cooling process in seconds.
        return a model equation to obtain temperature T
        at time t '''
        
    return (Ti-Ta)*np.exp((-t)/c) + Ta

print(model(0, 100, 0, 10))
print(model(10, 100, 0, 10))

ts = np.linspace(0, 3600, 4)
print(model(ts, 100, 20, 500))
