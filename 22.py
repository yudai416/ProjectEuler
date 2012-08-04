def buf2num(buf):
    return sum([ord(x) - 64 for x in buf])

f = open('names.txt', 'r')
bufs = f.read().replace('"', '').split(',')
f.close()
bufs.sort()
print sum([(i + 1) * buf2num(x) for i, x in enumerate(bufs)])
