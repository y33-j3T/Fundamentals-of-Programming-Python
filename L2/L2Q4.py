import math

def impact_velocity(h):
    ''' Given parameter h, calculate and 
        return the velocity (in metre per second) 
        with which an object falling from a height 
        of h meters will hit the ground '''
        
    return math.sqrt(2*9.81*h)

print(impact_velocity(10))