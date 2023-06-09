from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from random import randint
from math import gcd 
from gmpy2 import iroot 

from sympy.ntheory.modular import crt 

e = 17 # we already know about it
f = open("output.txt","r")
c_ls = []
n_ls = []
for i in range(17):
    n = int(f.readline().replace("n = ", "").strip())
    f.readline() # this line just read e
    c = int(f.readline().replace("c = ", "").strip())
    n_ls.append(n)
    c_ls.append(c)


def unPadding(msg):
    return msg[:msg[-1]]

flag = crt(n_ls, c_ls)[0]

flag, F = iroot(flag, e)
if F:
    print("Message found : ")
    print(unPadding(ltb(flag)))
else:
    print("Cannot find the flag.")

