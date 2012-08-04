num = 600851475143
i = 2

while num > i:
    if num % i == 0:
        num = num / i
    else:
        i = i + 1
print num
