from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
def generate_rsa_key(bitlen):
    p = getPrime(bitlen)
    while True:
        
        q = p + getRandomNBitInteger(bitlen // 2)
        if isPrime(q):
            return p, q

p, q = generate_rsa_key(1024)
flag = b"CTF{#################################################}"
flag = btl(flag)
e = 0x10001
n = p * q 
print(f"{n = }")
print(f"{e = }")
print(f"c = {pow(flag, e, n)}")

