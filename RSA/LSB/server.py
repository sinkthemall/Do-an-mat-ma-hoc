from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from random import randint
from math import gcd 
from gmpy2 import iroot 
from secret import flag
from sympy.ntheory.modular import crt 

def menu():
    print("1. Get encrypted secret")
    print("2. Get public key")
    print("3. Decrypt message")
    print("4. Exit")

def generate_rsa_key():
    e = 0x10001
    while True:
        p = getPrime(1024)
        q = getPrime(1024)
        if gcd(e, (p-1)*(q-1)) == 1:
            return p, q, e 
def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c,d, n) % 2

def challenge():
    p, q, e = generate_rsa_key()
    n = p*q 
    d = pow(e, -1,(p-1)* (q-1))
    while True:
        menu()
        cmd = input("> ").strip()
        if cmd == "1":
            print(encrypt(btl(flag), e, n))
            pass
        elif cmd == "2":
            print(f"{n = }")
            print(f"{e = }")
        elif cmd == "3":
            try:
                msg = int(input("The message you want to decrypt( in base 10): ").strip())
                if (msg <= 0 or msg >= n):
                    print("No sir")
                    continue
                print(f"Result : {decrypt(msg, d, n)}")
            except:
                print("Invalid number")
        elif cmd == "4":
            print("Terminating...")
            exit(0)
        else:
            print("Invalid command!")

challenge()

