tmp = list()
counts = dict()
fname = input("Enter file: ")
try :
    handle = open(fname)
except :
    print('Invalid File.')
    quit()
for line in handle :
    if line.startswith('From ') :
        line = line.rstrip()
        words = line.split()
        time = words[5]
        t = time.split(':')
        hour = t[0]
        counts[hour] = counts.get(hour, 0) + 1
for k, v in counts.items() :
    tmp.append( (k, v) )
    tmp = sorted(tmp)
for key, value in tmp :
    print(key, value)
