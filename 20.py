n = 100
num = eval('*'.join([str(x) for x in range(1, n+1)]))

sum = 0
while num > 0:
    sum = sum + num % 10
    num = num / 10

print sum
