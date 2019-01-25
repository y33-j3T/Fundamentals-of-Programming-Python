import matplotlib.pyplot as plt
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
    plot_data_f1 = create_plot_data(f1, -2, 2, 1001)
    plot_data_f2 = create_plot_data(f2, -2, 2, 1001)
    linef1, = plt.plot(plot_data_f1[0], plot_data_f1[1], 'b-', label='f1(x)')
    linef2 = plt.plot(plot_data_f2[0], plot_data_f2[1], 'r-', label='f2(x)')
    plt.xlabel('x')
    plt.grid(True)
    plt.legend()
    plt.show()

myplot()