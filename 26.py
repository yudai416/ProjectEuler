n = 1000
for y in [str(1.0 / x) for x in range(1, n)]:
    for i in range(1, 10):
        print i, y.count(str(i)),
    print y
