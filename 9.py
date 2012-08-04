import math

N = 1000
max = 500

def nine():
    for a in range(1, max):
        for b in range(a, max):
            c = math.sqrt(pow(a, 2) + pow(b, 2))
            if (a + b + c) == N:
                print a, b, c, a * b * c
                return


nine()
