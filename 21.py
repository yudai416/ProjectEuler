def make_divisor(st, ed):
    return [[x for x in range(1, n) if n % x == 0] for n in range(st, ed)]

sums = [0, 0] + [sum(x) for x in make_divisor(2, 10000)]
result = [x for i, x in enumerate(sums) if x < 10000 and i == sums[x] and i != x]
print result, sum(result)
