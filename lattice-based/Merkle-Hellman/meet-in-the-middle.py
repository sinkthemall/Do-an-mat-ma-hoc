f = open("output.txt", "r")
pub_key = eval(f.readline().strip().replace("Public key : ", ""))
enc_key = int(f.readline().strip().replace("Encrypted AES key : ", ""))
from json import loads 
msg = loads(f.readline().strip())
# from numba import jit
# from numba.core import types
# from numba.typed import Dict  

#@jit(fastmath = True, cache = True)
def bruteforce(ks_set):
    bf_solution = {}
    # Dict.empty(
    #     key_type = types.int64,
    #     value_type = types.int64
    # )
    for mask in range(0, (1<<len(ks_set))):
        sum = 0
        for i in range(len(ks_set)):
            if (mask >> i) & 1:
                sum += ks_set[i]
        bf_solution[sum] = mask 
    
    return bf_solution

#@jit(fastmath = True, cache = True)
def meet_in_the_middle(target, ks_set):
    n = len(ks_set)
    m = n//2
    ks_set1 = ks_set[:m]
    ks_set2 = ks_set[m:]
    bf_solution = bruteforce(ks_set2)
    keyset = []
    for mask in range(0, 1<<m):
        sum = 0
        for i in range(m):
            if (mask >> i) & 1:
                sum += ks_set1[i]
        try:
            solution = mask | (bf_solution[target - sum] << m)
            keyset.append(solution)
        except:
            pass
    if len(keyset):
        return keyset
    else:
        return None

from hashlib import sha256 
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Cipher import AES  
from Crypto.Util.Padding import unpad
keyset = meet_in_the_middle(enc_key, pub_key)
if keyset == None:
    print("Cannot find the solution!!!")
else:
    iv = bytes.fromhex(msg["iv"])
    enc = bytes.fromhex(msg["encrypted_message"])
    print("Possible message found:")
    for key in keyset:
        AESkey = sha256(ltb(key)).digest()[:16]
        cipher = AES.new(AESkey, AES.MODE_CBC, iv)
        try:
            print("Message found : ")
            print(unpad(cipher.decrypt(enc), 16))
        except:
            pass
