def cf_expansion(a,b):
    ls = []
    ls.append(a//b)
    a,b = b, a%b
    while(b!=0):
        ls.append(a // b)
        a , b = b, a%b
    return ls
import math
def cf_convergent(ls):
    n = []
    d = []
    for i in range(len(ls)):
        if (i == 0):
            n.append(ls[i])
            d.append(1)
        elif i == 1:
            n.append(ls[1]*ls[0] + 1)
            d.append(ls[1])
        else:
            n.append(n[i-1]*ls[i] + n[i-2])
            d.append(d[i-1]*ls[i] + d[i-2])
        yield n[i],d[i]

def solve(B,P):
    delta = B*B - 4*P
    if (delta<0):
        return 0,0
    rdel = math.isqrt(delta)
    return (B + rdel)//2, (B - rdel)//2

def find_d(n,e):
    for k,d in cf_convergent(cf_expansion(e,n)):
        if (k==0):
            continue
        phin = (e*d - 1)//k
        sum = n - phin + 1
        p, q = solve(sum, n)
        if (p*q==n):
            return d
    return 0

from Crypto.Util.number import long_to_bytes

f = open("output.txt", "r")
n = int(f.readline().replace("n = ", "").strip())
e = int(f.readline().replace("e = ", "").strip())
c = int(f.readline().replace("c = ", "").strip())
d = find_d(n,e)
if d!= 0:
    print("Message found : ")
    print(long_to_bytes(pow(c,d,n)))
else:
	print("Failed to factor n!")



