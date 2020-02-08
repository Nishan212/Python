# python code to find the sum of all the numbers present in a file 

import re
sum = 0
fname = input("Enter file name: ")
try :
    handle = open(fname)
except :
    print("Invalid file name.")
    quit()
for line in handle :
    lst = re.findall('[0-9]+', line)
    for n in lst :
        try :
            num = int(n)
            sum = sum + num
        except :
            continue
print(sum)
