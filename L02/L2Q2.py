import math

def fall_time(h):
    ''' Given parameter h, calculate and 
        return the time (in seconds) needed 
        for an object falling from a tower 
        of height h (in meters) to hit the ground 
        (ignoring air friction) '''
        
    return math.sqrt(2*h/9.81)

print(fall_time(10))