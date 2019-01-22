import matplotlib.pyplot as plt
from scipy.optimize import brentq
import math

def f1(x):
    return math.cos(2*math.pi*x)*math.e**(-(x*x))

def f2(x):
    return math.log(x+2.2)

def create_plot_data(f, xmin, xmax, n):
    ''' Given parameters f, xmin, xmax and n, 
         return a tuple (xs, ys) where xs and ys are 
         two sequences, each containing n numbers '''
         
    x = [(xmin + i*(xmax-xmin)/(n-1)) for i in range(n)]
    y = [f(num) for num in x]
    return x, y

def myplot():
    ''' Plot f1(x) and f2(x) '''
    
    plot_data_f1 = create_plot_data(f1, -2, 2, 1001)
    plot_data_f2 = create_plot_data(f2, -2, 2, 1001)
    linef1, = plt.plot(plot_data_f1[0], plot_data_f1[1], 'b-', label='f1(x)')
    linef2 = plt.plot(plot_data_f2[0], plot_data_f2[1], 'r-', label='f2(x)')
    plt.xlabel('x')
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.pause(1)
    plt.close()

def find_cross():
    f = lambda x: f1(x)-f2(x)
    ans = brentq(f, 0, 2, full_output=True)
    
    return ans

myplot()
print(find_cross())
