# Python code to find the average spam confidence present in the file 'mbox-short.txt'
# Needs: 'mbox-short.txt'
avg = 0.0
sum = 0.0
n = 0
filename = input('Enter file name:')
try :
    handle = open (filename, 'r')
except :
    print ('Error loading file')
    quit()
for line in handle :
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    n = n + 1
    pos = line.find(':')
    try :
        data = float(line[pos + 1 :])
    except :
        print('error')
    sum += data
    avg = sum / n
print ('Average spam confidence:' , avg)
