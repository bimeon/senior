from os.path import isfile

file_name = 'data/test.txt'

if isfile(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()

    for line in lines:
        print('>>>', line.strip())