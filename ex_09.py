# Python code to sort the words present in a file (case-insensitive)

fname = input('Enter file name: ')
try :
    handle = open(fname)
except :
    print('Invalid filename')
    quit()
lst = list()
for line in handle :
    sl = line.split()
    #print(sp)
    for word in sl :
        if not word in lst :
            lst.append(word)
lst = sorted(lst, key = lambda s : s.lower())
for word in lst:
    print(word + " ", end = '')
