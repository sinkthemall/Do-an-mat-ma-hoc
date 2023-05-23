from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from math import gcd 


f = open("output.txt", "r")
n = int(f.readline().replace("n = ", "").strip())
e = int(f.readline().replace("e = ", "").strip())
c = int(f.readline().replace("c = ", "").strip())

for i in range(2, (1<<20)):
    if isPrime(i) and gcd(i, n) != 1:
        p = i 
        q = n // i
        print(f"Found {p = }")
        print(f"Found {q = }")
        d = pow(e, -1, (p-1)*(q-1))
        print(ltb(pow(c,d,n)))
        break