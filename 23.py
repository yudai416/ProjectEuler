def make_divisor(st, ed):
    r = [[x for x in range(1, n / 2 + 1) if n % x == 0] for n in range(st, ed)]
    return r

#sums = [0, 0] + [sum(x) for x in make_divisor(2, 24)]
#print sums
sums = [0, 0] + [sum(x) for x in make_divisor(2, 28124)]
abundants = [i for i, x in enumerate(sums) if i < x]
print abundants
