import itertools

pum = [x for x in itertools.permutations(range(10), 10)][1000000 - 1]
buf = ''
for i in pum:
    buf = buf + str(i)
print buf
