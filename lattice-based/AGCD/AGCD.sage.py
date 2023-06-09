

# This file was *autogenerated* from the file AGCD.sage
from sage.all_cmdline import *   # import sage library

_sage_const_127 = Integer(127); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_16 = Integer(16); _sage_const_20 = Integer(20)
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


security = _sage_const_127 

def decrypt_key(enc, sk):
    msg = _sage_const_0 
    for i in enc[::-_sage_const_1 ]:
        bit = (i % sk ) % _sage_const_2 
        msg <<= _sage_const_1 
        msg |= bit 
    return msg 

def AES_decrypt(iv, ciphertext : bytes, secretkey, enc_key):
    key = ltb(decrypt_key(enc_key, secretkey))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), _sage_const_16 )
    return plaintext

def recover_key(idx):
    N = len(pubkey)
    if N >_sage_const_20 :
        N = _sage_const_20 
    ma = [[_sage_const_0  for i in range(N)] for j in range(N)]
    ma[_sage_const_0 ][_sage_const_0 ] = _sage_const_2  ** (security + _sage_const_1 )
    for i in range(_sage_const_1 , N):
        ma[i][i] = -pubkey[idx]
        ma[_sage_const_0 ][i] = pubkey[i]
    
    newma = matrix(ma)
    newma = newma.LLL()
    for row in newma:
        ok = abs(row[_sage_const_0 ])
        if ok % _sage_const_2 **(security + _sage_const_1 ) == _sage_const_0 :
            q = ok // _sage_const_2 **(security + _sage_const_1 ) 
            p = pubkey[idx] // q
            return p 
    return None 



if len(pubkey) > _sage_const_20 :
    sk = _sage_const_0 
    for i in range(_sage_const_20 , len(pubkey)):
        ok = recover_key(i)
        if ok == None:
            pass 
        else:
            sk = gcd(sk, ok)
        # print(f"p : {p}")
else:
    sk = recover_key(_sage_const_0 )

if sk == None or sk == _sage_const_1  or  sk == _sage_const_0 :
    print("Key not found!")
else:
    print(f"Secret key found: {sk}")
    assert(isPrime(int(sk)))
    print("Message found : ")
    print(AES_decrypt(iv, ciphertext, sk, enc_key))


