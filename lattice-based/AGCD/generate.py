from Crypto.Util.number import getPrime, long_to_bytes as ltb, bytes_to_long as btl
from Crypto.Util.Padding import pad, unpad
from Crypto.Random.random import getrandbits
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
from json import loads, dumps 

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

def encrypt_key(m, pubkey):
    enc = []
    while m:
        bit = m & 1 
        enc.append(encryptbit(bit, pubkey))
        m >>= 1 
    return enc 

def decrypt_key(enc, privatekey):
    m =0 
    for i in enc[::-1] :
        bit = (i % privatekey) % 2
        m <<=1
        m |= bit 
    return m 

def AES_encrypt(msg : str , pubkey):
    iv = get_random_bytes(16)
    key = get_random_bytes(16)
    pad_msg = pad(msg.encode(), 16)
    enc_key = encrypt_key(btl(key), pubkey)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad_msg)
    return enc_key, iv, ciphertext

def AES_decrypt(iv, ciphertext : bytes, secretkey, enc_key):
    key = ltb(decrypt_key(enc_key, secretkey))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext


bitlen = 512
security = 128
privatekey, pubkey = key_generate(bitlen, security, 128)
flag = input("Enter message to encrypt: ").strip()
enc_key, iv, ciphertext = AES_encrypt(flag, pubkey)
ok = {"iv" : iv.hex(), "ciphertext" : ciphertext.hex()}

f = open("output.txt", "w")
f.write(f"Public key : {pubkey}\n")
f.write(f"Encrypted AES key : {enc_key}\n")
f.write(f"{dumps(ok)}\n")

f.close()
print(AES_decrypt(iv, ciphertext, privatekey, enc_key))
print("Writing result to output.txt - completed!!!")


