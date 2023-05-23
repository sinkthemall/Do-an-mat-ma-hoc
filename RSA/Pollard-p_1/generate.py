from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from math import gcd 


def gen_smooth_prime_above(bitlen, smoothness = 16):
    p = 2
    while p.bit_length() + smoothness < bitlen:
        p = p * getPrime(smoothness)
    while True:
        a = getPrime(smoothness)
        if isPrime(a * p + 1):
            return a * p + 1

def generate_rsa_key():
    while True:
        p = gen_smooth_prime_above(1024, 16)
        q = getPrime(p.bit_length())
        if gcd(0x10001, (p-1)*(q-1)) == 1:
            return p, q
        
p, q = generate_rsa_key()
n = p* q 
flag = input("Enter message to encrypt: ")
flag = btl(flag.encode())
e = 0x10001
c = pow(flag, e, n)

f = open("output.txt", "w")
f.write(f"{n = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")
f.close()

print(f"{n = }\n")
print(f"{e = }\n")
print(f"{c = }\n")


print("Writing result to output.txt - completed!!!")