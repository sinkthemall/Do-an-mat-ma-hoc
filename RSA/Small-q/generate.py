from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from math import gcd 


def generate_rsa_key(bitlength):
    # 1 prime'length will be below 20 bit
    while True:
        q = getPrime(20)
        p = getPrime(bitlength)
        if gcd(0x10001, (p-1)*(q-1)) == 1:
            return p,q 

p, q = generate_rsa_key(1024)
n = p*q 
while True:
    flag = input("Enter message to encrypt: ").strip()
    flag = btl(flag.encode())
    if gcd(flag, q) != 1:
        print("Last message you enter is no valid, enter another message: ")
    else:
        break

e = 0x10001
c = pow(flag, e, n)
f = open("output.txt","w")
f.write(f"{n = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")

print(f"{n = }\n")
print(f"{e = }\n")
print(f"{c = }\n")

f.close()

print("Writing result to output.txt - completed!!!")
