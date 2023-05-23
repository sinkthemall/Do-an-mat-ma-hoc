from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from random import randint
from math import gcd 
from gmpy2 import mpz 

from primefac import pollard_pm1, rpn
f = open("output.txt","r")
n = int(f.readline().replace("n = ", "").strip())
e = int(f.readline().replace("e = ", "").strip())
c = int(f.readline().replace("c = ", "").strip())

def special_pow(base, exp : int, mod):
    assert(exp.bit_length() <= 20 ) # only use this for bitlength(exp) <=20  or this could be very slow
    ans = mpz(base) 
    modder = mpz(mod)
    for i in range(1, exp + 1):
        ans = pow(ans, mpz(i), modder)
    return ans 

def pm1(n, guessy_smoothness):
    while True:
        g = randint(1, 100000)
        print(f"Testing {g = }") 
        exp = getRandomNBitInteger(guessy_smoothness)
        a = special_pow(g, exp, n)
        if gcd(a - 1, mpz(n)) != 1 and gcd(a-1, mpz(n)) != mpz(n):
            p = gcd(a-1, n)
            q = n // p
            return p, q

# for primefac option, this could be very slow when smoothness is about 20 or more

# p = pollard_pm1(n)
# print(p)
# q = n // p

p, q = pm1(n, 17)
assert( p* q ==n)
d = pow(e, -1, (p-1)*(q-1))
print(ltb(pow(c,d,n)))

