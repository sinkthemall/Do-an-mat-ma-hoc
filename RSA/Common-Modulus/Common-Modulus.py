from Crypto.Util.number import long_to_bytes as ltb
from math import gcd 

def egcd(a,b,c):
    assert(gcd(a, b) == c)
    x0, y0 = 1, 0 
    x1, y1 = 0, 1
    r0 = a
    r1 = b 
    while r1 != 0:
        q = r0 // r1 
        nr = r0 % r1 
        nx = x0 - q * x1 
        ny = y0 - q * y1 
        x0, y0 = x1, y1 
        x1, y1 = nx, ny 
        r0, r1 = r1, nr 
    return (x0, y0)

f = open("output.txt", "r")
n = int(f.readline().strip().replace("n = ", ""))
e1 = int(f.readline().strip().replace("e1 = ", ""))
e2 = int(f.readline().strip().replace("e2 = ", ""))
c1 = int(f.readline().strip().replace("c1 = ", ""))
c2 = int(f.readline().strip().replace("c2 = ", ""))
x, y = egcd(e1, e2, 1)

m = (pow(c1, x, n) * pow(c2, y, n))% n
print("Message found : ")
print(ltb(m))