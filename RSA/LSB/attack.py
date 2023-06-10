from pwn import *

s = remote("localhost", 9000)

def get_encrypted_secret():
    s.sendlineafter(b"> ", b"1")
    return int(s.recvline(0).decode())

def get_pubkey():
    s.sendlineafter(b"> ", b"2")
    n = int(s.recvline(0).decode().replace("n = ", ""))
    e = int(s.recvline(0).decode().replace("e = ", ""))
    return n, e 

def oracle(c : int):
    s.sendlineafter(b"> ", b"3")
    s.sendlineafter(b"base 10): ", str(c).encode())
    s.recvuntil(b"Result : ")
    return int(s.recvline(0).decode())


def attack(N ,e, c, oracle):
    left = 0
    right = N
    while right - left > 1:
        c = c * pow(2, e, N) % N
        if oracle(c) == 0:
            right = (right + left) // 2
        else:
            left = (right + left) // 2
        #print(left, right)
    return right 
n, e = get_pubkey()
secret = get_encrypted_secret()

from Crypto.Util.number import long_to_bytes as ltb 
print("Message found : ")
print(ltb(attack(n, e, secret, oracle=oracle)))
