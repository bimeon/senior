file_name = 'data/test.txt'

f = open(file_name, 'w')
f.write('hello world!\n')
f.close()

# append 모드
f=open(file_name, 'a')
f.write('hello class')
f.close()