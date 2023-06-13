from Crypto.Util.number import getPrime, long_to_bytes as ltb, bytes_to_long as btl
from random import randint
from math import gcd
p, q = getPrime(1024), getPrime(1024)

n = p*q 
while True:
    e1 = randint(2, 1000000) * 2 + 1
    e2 = randint(2, 1000000) * 2 + 1
    if e1 == e2:
        continue
    if gcd(e1, (p-1)*(q-1)) != 1:
        continue
    if gcd(e2, (p-1)*(q-1)) != 1:
        continue
    if gcd(e1, e2) != 1:
        continue
    break

flag = btl(input("Enter message to encrypt : ").strip().encode())
c1 = pow(flag, e1, n)
c2 = pow(flag, e2, n)


f = open("output.txt", "w")
f.write(f"{n = }\n")
f.write(f"{e1 = }\n")
f.write(f"{e2 = }\n")
f.write(f"{c1 = }\n")
f.write(f"{c2 = }\n")

f.close()

print("Writing result to output.txt - completed!!!")

