# example python code to calculate 'pay' that depends on parameters 'hour' and 'rate'

def computepay(hour, rate):
    if hour <= 40.0:
        p = hour * rate
    elif hour > 40.0:
        p = (40 * rate) + ((hour - 40) * 1.5 * rate)
    return p


hour = input("Enter hours:")
rate = input("Enter rate:")
hour = float(hour)
rate = float(rate)
pay = computepay(hour, rate)
print (pay)
