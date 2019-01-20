import math

def seq_sqrt(xs):
    sqrt_num=[]
    for x in xs:
        sqrt_num.append(math.sqrt(x))
    return sqrt_num

print(seq_sqrt([1, 2, 3, 4, 5]))
