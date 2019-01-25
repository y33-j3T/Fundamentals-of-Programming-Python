def f(x):
    return x*10

def f2(x):
    return 0

def create_plot_data(f, xmin, xmax, n):
    ''' Given parameters f, xmin, xmax and n, 
         return a tuple (xs, ys) where xs and ys are 
         two sequences, each containing n numbers '''
         
    x = [(xmin + i*(xmax-xmin)/(n-1)) for i in range(n)]
    y = [f(num) for num in x]
    return x, y

print(create_plot_data(f, -1, 1, 2))
print(create_plot_data(f, 0, 2, 5))
print(create_plot_data(f2, 0, 1.5, 4))