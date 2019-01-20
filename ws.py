import os
os.chdir(r'C:\users\yee jet tan\desktop')
file = open('data.csv', 'r')

def line_averages(filename):
    data = filename.readlines()
    answer = list()
    for d in data:
        total=0.0
        s = d.split(',')
        for num in s:
            num = float(num)
            total = total + num
        answer.append(total/len(s))
    return answer

print(line_averages(file))

file.close()
# ['1,2\n', '1,1,1,1\n', '-1,0,1\n', '42,17']
