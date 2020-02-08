# Python code to find the number of lines that start with the input 'word'

count = 0
fname = input('Enter file name: ')
word = input('Enter a word: ')
try :
    handle = open(fname)
except :
    print('invalid file name!')
for line in handle :
    if not line.startswith(word + ' ') :
        continue
    else :
        count = count + 1
        line = line.rstrip()
        lst = line.split()
print('There is/are', count, 'line/s in the file with', word, 'as the first word')
