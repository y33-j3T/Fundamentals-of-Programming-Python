import math

def swing_time(L):
    ''' Given parameter L, compute and return 
        the time T [in seconds] needed for an 
        idealized pendulum of length L [in meters] 
        to complete a single oscillation '''
        
    return 2*math.pi*math.sqrt(L/9.81)

print(swing_time(1))