def fib(prev1, prev2):
    return prev1 + prev2, prev1

i = 3
prev1 = 1
prev2 = 1

while 1:
    prev1, prev2 = fib(prev1, prev2)
    if len(str(prev1)) == 1000:
        print i
        break
    i = i + 1
