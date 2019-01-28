import math

def std_dev(x):
    mu = sum(x)/len(x)
    std_dev = math.sqrt(sum([(val-mu)**2 for val in x])/(len(x)-1))
    return std_dev

print(std_dev([1.0, 1.0]))
print(std_dev([1.0, 2.0]))
