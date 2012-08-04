def divisor(num):
    i = 0
    count = 0
    while i <= num/2:
        i = i + 1 
        if num % i == 0:
            count = count + 1
    return count+1


if __name__ == '__main__':
    i = 11900
    tri = 0
    while 1:
        i = i + 1
        tri = sum(range(i+1))
        #print tri, i, divisor(tri)
        if divisor(tri) >= 501:
            print tri, i, divisor(tri)
            break
        if i % 100 == 0:
            print tri, i, divisor(tri)
