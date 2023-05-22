f = open("output.txt")
ls = []
e = 0x10001
for i in range(17):
    n = f.readline().replace("n = ", "").strip()
    n = int(n)
    f.readline()
    c = int(f.readline().replace("c = ", "").strip())
    f.readline()
    ls.append((n, c))

from math import gcd 
from Crypto.Util.number import long_to_bytes as ltb
for n1, c1 in ls:
    for n2, c2 in ls:
        if n1 != n2:
            if gcd(n1, n2) != 1:
                p = gcd(n1,n2)
                q = n1 // p
                d = pow(e, -1, (p-1)*(q-1))
                print(ltb(pow(c1, d, n1)))
                exit(0)