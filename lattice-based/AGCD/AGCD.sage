from Crypto.Util.number import getPrime, long_to_bytes as ltb, bytes_to_long as btl, isPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES 
from json import loads, dumps 
f = open("output.txt", "r")

pubkey = eval(f.readline().strip().replace("Public key : ", ""))
enc_key = eval(f.readline().strip().replace("Encrypted AES key : ", ""))
enc_message = loads(f.readline().strip())
iv = bytes.fromhex(enc_message["iv"])
ciphertext = bytes.fromhex(enc_message["ciphertext"])


security = 127

def decrypt_key(enc, sk):
    msg = 0
    for i in enc[::-1]:
        bit = (i % sk ) % 2
        msg <<= 1
        msg |= bit 
    return msg 

def AES_decrypt(iv, ciphertext : bytes, secretkey, enc_key):
    key = ltb(decrypt_key(enc_key, secretkey))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext

def recover_key(idx):
    N = len(pubkey)
    if N >20:
        N = 20
    ma = [[0 for i in range(N)] for j in range(N)]
    ma[0][0] = 2 ^ (security + 1)
    for i in range(1, N):
        ma[i][i] = -pubkey[idx]
        ma[0][i] = pubkey[i]
    
    newma = matrix(ma)
    newma = newma.LLL()
    for row in newma:
        ok = abs(row[0])
        if ok % 2^(security + 1) == 0:
            q = ok // 2^(security + 1) 
            p = pubkey[idx] // q
            return p 
    return None 



if len(pubkey) > 20:
    sk = 0
    for i in range(20, len(pubkey)):
        ok = recover_key(i)
        if ok == None:
            pass 
        else:
            sk = gcd(sk, ok)
        # print(f"p : {p}")
else:
    sk = recover_key(0)

if sk == None or sk == 1 or  sk == 0:
    print("Key not found!")
else:
    print(f"Secret key found: {sk}")
    assert(isPrime(int(sk)))
    print("Message found : ")
    print(AES_decrypt(iv, ciphertext, sk, enc_key))

