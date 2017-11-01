import math
def modexp_lr(a, b, n):
    r = 1
    for bit in reversed(bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    return r

def bits_of_n(n):
    bits = []
    while n:
        bits.append(n % 2)
        n /= 2
    return bits

def eulers_criterion():
    t_c = input()
    while t_c > 0:
        a,m = map(int, raw_input().strip().split(' '))
        if a != 0:
            if modexp_lr(a, (m-1)/2, m) == 1:
                print "YES"
            else:
                print "NO"
        else:
            print "YES"
        t_c -= 1

eulers_criterion()