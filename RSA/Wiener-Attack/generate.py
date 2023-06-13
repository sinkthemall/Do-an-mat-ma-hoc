from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from math import gcd 


def generate_rsa_key(bitlength):
    p = getPrime(bitlength // 2)
    q = getPrime(bitlength // 2)
    while True:
        d = getRandomNBitInteger(bitlength // 4 - 5)
        if d >= pow(2, bitlength // 4 - 1) // 3:
            continue
        if gcd(d, (p-1)*(q-1)) == 1:
            e = pow(d, -1, (p-1)*(q-1))
            return p, q, e 

p ,q, e = generate_rsa_key(2048)
n = p * q 
flag = input("Enter message to encrypt: ").strip()

flag = btl(flag.encode())
c = pow(flag, e, n)
print(f"{n = }")
print(f"{e = }")
print(f"{c = }")

f = open("output.txt", "w")
f.write(f"{n = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")
f.close()
print("Writing result to output.txt - completed!!!")
