try:
    f = open('result10.txt')
    buf = f.read()
    #print buf.split()
    sums = eval('+'.join(buf.strip().split(',')))
    print sums
except:
    print 'error'
