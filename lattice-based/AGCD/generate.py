from Crypto.Util.number import getPrime, long_to_bytes as ltb, bytes_to_long as btl
from Crypto.Random.random import getrandbits

def key_generate(bitlength, security, mlen):
    p = getPrime(bitlength)
    pubkey = []
    for i in range(mlen):
        q = getrandbits(bitlength)
        noise = getrandbits(security)
        pubkey.append(p * q + 2 * noise)
    return p, pubkey
def encryptbit(m, pubkey):
    enc = 0
    for i in pubkey:
        k = getrandbits(1)
        if k:
            enc += i 
    return enc + m 

def encrypt(m, pubkey):
    enc = []
    while m:
        bit = m & 1 
        enc.append(encryptbit(bit, pubkey))
        m >>= 1 
    return enc 

def decrypt(enc, privatekey):
    m =0 
    for i in enc[::-1] :
        bit = (i % privatekey) % 2
        m <<=1
        m |= bit 
    return m 


bitlen = 1024
security = 128
privatekey, pubkey = key_generate(bitlen, security, 128)
flag = btl(input("Enter message to encrypt: ").strip().encode())
enc = encrypt(flag, pubkey)

f = open("output.txt", "w")
f.write(f"Public key : {pubkey}\n")
f.write(f"Encrypted message : {enc}\n")
f.close()

print("Writing result to output.txt - completed!!!")


