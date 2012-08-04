buf = [[int(y) for y in x.split(' ')] for x in open('18.txt', 'r')]

for i in reversed(range(len(buf)-1)):
    for j in range(len(buf[i])):
        #print i, j, buf[i][j], buf[i+1][j:j+2],
        buf[i][j] = buf[i][j] + max(buf[i+1][j:j+2])
        #print buf[i][j]

print buf[0][0]
