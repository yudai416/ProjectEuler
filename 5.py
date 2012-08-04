def aaa(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def bbb(num, prime):
    for i in prime:
        n = 0
        if num % i == 0:
            n = n + 1
            num = num / i
            while 1:
                if num % i != 0:
                    break
                n = n + 1
                num = num / i
            if n > prime[i]:
                prime[i] = n


prime = {}
for i in range(2, 21):
    if aaa(i):
        prime[i] = 1
    else:
        bbb(i, prime)

product = 1
for i in prime:
    product = product * pow(i, prime[i])

print product
