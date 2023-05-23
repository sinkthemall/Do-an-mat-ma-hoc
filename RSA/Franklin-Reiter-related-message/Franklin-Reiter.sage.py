

# This file was *autogenerated* from the file Franklin-Reiter.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0)
from sage.all import *
f = open("./output.txt", "r")
N = int(f.readline().replace("n = ", "").strip())
e = int(f.readline().replace("e = ", "").strip())
a0 = int(f.readline().replace("a0 = ", "").strip())
b0 = int(f.readline().replace("b0 = ", "").strip())
C0 = int(f.readline().replace("c0 = ", "").strip())
a1 = int(f.readline().replace("a1 = ", "").strip())
b1 = int(f.readline().replace("b1 = ", "").strip())
C1 = int(f.readline().replace("c1 = ", "").strip())
a2 = int(f.readline().replace("a2 = ", "").strip())
b2 = int(f.readline().replace("b2 = ", "").strip())
C2 = int(f.readline().replace("c2 = ", "").strip())

P = PolynomialRing(Zmod(N), names=('x',)); (x,) = P._first_ngens(1)
f1 = (a1 * x + b1) ** e  -C1
f2 = (a2 * x + b2) ** e  - C2
f0 = (a0 * x + b0) ** e - C0

from Crypto.Util.number import long_to_bytes as ltb 
def gcd(a,b):
    if  b == _sage_const_0 :
        return a.monic()
    else:
        return gcd(b, a%b)

flag = gcd(gcd(f1,f2), f0)[_sage_const_0 ]
print(ltb(int(N - flag)))

