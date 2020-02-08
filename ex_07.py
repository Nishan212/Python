# Python code open file in read mode and remove whitespaces on the right side
# of the lines and the print the line in Uppercase

handle = open (filename, 'r')
for line in handle :
    line = line.rstrip()
    print(line.upper())
