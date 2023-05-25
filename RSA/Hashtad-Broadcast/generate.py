from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from random import randint
from math import gcd 
from gmpy2 import mpz 

def Padding(msg, length):
    ok = msg + bytes([len(msg)]) * (length - len(msg))
    return ok

def unPadding(msg):
    return msg[:msg[-1]]

            
def generate_rsa_keys(e = 17):
    rsa_keys = []
    for i in range(e):
        while True:

            p = getPrime(1024)
            q = getPrime(1024)
            n = p * q 
            if gcd(e, (p-1)*(q-1)) == 1:
                break
        d = pow(e, -1, (p-1)*(q-1))
        rsa_keys.append((n, e, d))
    return rsa_keys

flag = input("Enter message to encrypt: ").strip()

flag = btl(Padding(flag.encode(), 255)) # this is use to prevent user enter short message
                                   # of course it still can be found by using some special technique, or even be exploited

rsakey =  generate_rsa_keys()
f = open("output.txt", "w")

for n, e, d in rsakey:
    f.write(f"{n = }\n")
    f.write(f"{e = }\n")
    c = pow(flag, e, n)
    f.write(f"{c = }\n")

f.close()
print("Writing result to output.txt - completed!!!")
