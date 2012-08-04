def aaa(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        else:
            i = i + 1
    return True


count = 0
num = 1
while 1:
    num = num + 1
    if aaa(num):
        count = count + 1
        if count % 100 == 0:
            print num, count
    if count == 10001:
        print num
        break
