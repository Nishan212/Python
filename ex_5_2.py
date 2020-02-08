# code to find max amd min of set of input numbers

largest = None
smallest = None
while True :
    sval = input('Enter a number (Enter \'done\' to exit):')
    if sval == 'done' :
        break
    try :
        fval = int (sval)
    except :
        print ('Invalid input: input should be integer (number)!')
        continue
    if smallest is None :
        smallest = fval
    elif fval < smallest :
        smallest  = fval
    if largest is None :
        largest = fval
    elif fval > largest :
        largest = fval
print ('Maximum is', largest)
print('Minimum is', smallest)
