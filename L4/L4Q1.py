def line_averages(filename):
    ''' Given parameter filename, 
        open and read csv file with filename filename, 
        compute the average value for every line
        and return the average values in a list '''
    file = open(filename, 'r')
    data = file.readlines()
    answer = []
    for d in data:
        total=0.0
        s = d.split(',')
        for num in s:
            num = float(num)
            total = total + num
        answer.append(total/len(s))
    return answer
    file.close()

print(line_averages('data.csv'))