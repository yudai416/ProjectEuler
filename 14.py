def suretu(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def count(n):
    count = 0
    while n > 1:
        n = suretu(n)
        count = count + 1
        #print n
    #print 'count =', count
    return count

max_count = 0
for n in range(1,1000000):
    n_count = count(n)
    if n_count > max_count:
        max_count = n_count
        print 'n =', n, max_count
