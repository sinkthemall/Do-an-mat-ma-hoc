from sage.all import *
f = open("output.txt", "r")
pub_key = eval(f.readline().strip().replace("Public key : ", ""))
enc_key = int(f.readline().strip().replace("Encrypted AES key : ", ""))
from json import loads 
msg = loads(f.readline().strip())

n = len(pub_key)
def check_row(row):
    for i in row:
        if not (-1/2<= i <=1/2):
            return False
    return True

def find_secret_key():
    ma = [[0 for i in range(n + 1)] for j in range(n + 1)]
    ma[0][0] = enc_key

    for i in range(n):
        ma[0][i + 1] = -pub_key[i]
        ma[i + 1][0] = -1/2
        ma[i + 1][i + 1] = 1
    ma = matrix(ma)
    newma = ma.transpose().LLL()
    ans = 0
    for row in newma:
        if row[0] == 0:
            if check_row(row[1:]):
                for j in row[1:][::-1]:
                    if j == -1/2:
                        ans = ans << 1
                    else:
                        ans = (ans << 1) | 1
                return ans 
    return None

from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad
key = ltb(find_secret_key())
if key == None:
    print("Cannot recover secret key!!!")
else:
    iv = bytes.fromhex(msg["iv"])
    enc = bytes.fromhex(msg["encrypted_message"])

    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(unpad(cipher.decrypt(enc), 16))
