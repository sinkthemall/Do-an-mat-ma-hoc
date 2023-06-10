from sage.all import *
p = 310717010502520989590157367261876774703
a = 2
b = 3
Fp = GF(p)
EC = EllipticCurve(Fp, [a, b])
G = EC(179210853392303317793440285562762725654, 105268671499942631758568591033409611165)
Bob_key = EC(272640099140026426377756188075937988094, 51062462309521034358726608268084433317)
Alice_key = EC(280810182131414898730378982766101210916, 291506490768054478159835604632710368904)
enc = {'iv': '07e2628b590095a5e332d397b8a59aa7', 'encrypted_flag': '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'}

#finding secret key over smooth order elliptic curve
def find_key():
    Alice_secret_key = discrete_log(Alice_key, G, ord = EC.order(), operation= "+")
    return Alice_secret_key

A_secret_key = find_key()
share_key = A_secret_key * Bob_key 
final_share_key = share_key.xy()[0]


print(f"Alice secret key found: {A_secret_key}")
iv = bytes.fromhex(enc["iv"])
encrypted_flag = bytes.fromhex(enc["encrypted_flag"])
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1
aes_key = sha1(str(final_share_key).encode()).digest()[:16]

cipher = AES.new(aes_key, AES.MODE_CBC, iv)
print(f"Message found : ")
print(unpad(cipher.decrypt(encrypted_flag), 16))
