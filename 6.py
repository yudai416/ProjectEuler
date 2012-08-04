sum1 = 0
sum2 = 0
for i in range(1, 101):
    sum1 = sum1 + pow(i, 2)
    sum2 = sum2 + i

print pow(sum2, 2) - sum1
