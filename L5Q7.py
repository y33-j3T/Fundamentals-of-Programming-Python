def traffic_light(load):
    ''' Given parameter load, return string
        "green" for values of load below 0.7,
        "amber" for values of load equal to or greater than 0.7 but smaller than 0.9,
        "red" for values of load equal to or greater than 0.9 '''
        
    if(load<0.7):
        return 'green'
    elif(load>=0.7 and load<0.9):
        return 'amber'
    else:
        return 'red'
    
print(traffic_light(0.5))