# Python code to find the highest frequency of the user-mailID in the file 'mbox-short.txt'
# Needs: 'mbox-short.txt'

counts = dict()
words = list()
fname = input("Enter file name: ")
try:
    handle = open(fname)
except :
    print("Invalid filename.")
    quit()
for line in handle :
    if line.startswith('From ') :
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1
highword = None
highcount = None
for k, v in counts.items() :
        if highcount is None or v > highcount :
            highcount = v
            highword = k
print(highword, ':', highcount)
