i = 2
sum = 2
fib = [1, 2]
max = 4000000

while 1:
    fib.append(fib[i-2] + fib[i-1])
    if fib[i] > max:
        break
    elif fib[i] % 2 == 0:
        sum = sum + fib[i]
    i = i + 1

print sum
