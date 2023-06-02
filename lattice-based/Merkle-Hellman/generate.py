import random
from collections import namedtuple
import gmpy2
from Crypto.Util.number import isPrime, bytes_to_long, inverse, long_to_bytes
from os import urandom
from Crypto.Util.Padding import pad, unpad
from json import loads, dumps 

flag = input("Enter message to encrypt: ").strip()
PrivateKey = namedtuple("PrivateKey", ['b', 'r', 'q'])
#merkle hellman knapsack cryptosystem preprocessing------------------
def gen_private_key(size):
    s = 10000
    b = []
    for _ in range(size):
        ai = random.randint(s + 1, 2 * s)
        assert ai > sum(b)
        b.append(ai)
        s += ai
    while True:
        q = random.randint(2 * s, 32 * s)
        if isPrime(q):
            break
    r = random.randint(s, q)
    assert q > sum(b)
    assert gmpy2.gcd(q,r) == 1
    return PrivateKey(b, r, q)


def gen_public_key(private_key: PrivateKey):
    a = []
    for x in private_key.b:
        a.append((private_key.r * x) % private_key.q)
    return a


def encrypt(msg, public_key):
    assert len(msg) * 8 <= len(public_key)
    ct = 0
    msg = bytes_to_long(msg)
    for bi in public_key:
        ct += (msg & 1) * bi
        msg >>= 1
    return ct


def decrypt(ct, private_key: PrivateKey):
    ct = inverse(private_key.r, private_key.q) * ct % private_key.q
    msg = 0
    for i in range(len(private_key.b) - 1, -1, -1):
         if ct >= private_key.b[i]:
             msg |= 1 << i
             ct -= private_key.b[i]
    return long_to_bytes(msg)
#END section---------------------------------------------------------


#-------- AES section
from Crypto.Cipher import AES 
def AES_encrypt(key, msg):
    msg = pad(msg, 16)
    iv = urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(msg)
    return (iv, enc)

def AES_decrypt(key, encrypted, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(encrypted)
    return unpad(dec)
#END section---------


from hashlib import sha256 
#-------- Generate AES secret key and encrypt it, iv just let it stay the same, no need to encrypt it
key_length = 6
key = urandom(key_length)
AESkey = sha256(key).digest()[:16]
iv, enc = AES_encrypt(AESkey, flag.encode())
private_key = gen_private_key(len(key) * 8)
public_key = gen_public_key(private_key)
encrypt_key = encrypt(key, public_key)
assert(decrypt(encrypt_key, private_key) == key)
#END section-----------------------------------------------------------------------------------------



#-----------Final part-------------
q = {"iv" : iv.hex(), "encrypted_message" : enc.hex()}

f = open("output.txt", "w")
f.write(f"Public key : {public_key}\n")
f.write(f"Encrypted AES key : {encrypt_key}\n")
f.write(f"{dumps(q)}\n")
f.close()
#END section-----------------------

print("Writing result to output.txt - completed!!!")