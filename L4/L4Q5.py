def wc(filename):
    ''' Given parameter filename, calculate and
        return the number of words in file filename '''
    file = open(filename, 'r')
    return len(file.read().split())

print(wc('data.txt'))