import math

def max_divisor(num):
    i = int(math.sqrt(num))
    while i > 0:
        if num % i == 0:
            return i
        else:
            i = i - 1
    return 1
            
num = 997799
i = 3

while 1:
    if i % 100 == 0:
        num = num - 11
    elif i % 10 == 0:
        num = num - 110
    else:
        num = num - 1100
    divisor = max_divisor(num)
    if divisor < 1000 and num / divisor < 1000:
        print num, divisor, num / divisor
        break
    #print num, divisor, num / divisor, i 
    i = i + 1
