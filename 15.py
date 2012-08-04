def permutation(n):
    return eval('*'.join([str(x) for x in range(1,n+1)]))

def conbination(a, b):
    if a < b or a <= 0 or b <= 0:
        print 'error'
        return
    return permutation(a) / (permutation(b) * permutation(a-b))

print conbination(40, 20)
