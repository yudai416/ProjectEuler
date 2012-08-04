N = 2000000
#N = 10
n = N / 2 + 1
nums = range(3, N+1, 2)
sum = 2

while nums != []:
    num = nums.pop(0)
    sum = sum + num
    print num

    for i in nums:
        if i % num == 0:
            nums.remove(i)
            #print 'not', i#, #nums
    """
    while num <= N:
        num = num + prime
        try:
            nums.remove(num)
            #print 'num =', num
        except:
            pass
    """
print 'sum = ', sum
