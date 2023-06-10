from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from random import randint
from math import gcd 
from gmpy2 import iroot 

from sympy.ntheory.modular import crt 


def generate_rsa_key():
    e = 0x10001
    while True:
        p = getPrime(1024)
        q = getPrime(1024)
        if gcd(e, (p-1)*(q-1)) == 1:
            return p, q, e 

flag = input("Enter message to encrypt: ").strip()
flag = btl(flag.encode())

p, q, e = generate_rsa_key()
n = p * q 
c = pow(flag, e, n)

f = open("output.txt", "w")
f.write(f"{n = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")
f.write(f"Truncated p = {p & ((1 << (512 + 256)) - 1)}\n")

f.close()
print("Writing result to output.txt - completed!!!")
