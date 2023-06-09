from pwn import *
from Crypto.Util.number import long_to_bytes as ltb 

s = remote("localhost", 9000)

#get public key
s.sendlineafter(b"> ", b"2")
n = int(s.recvline(0).decode().replace("n = ", ""))
e = int(s.recvline(0).decode().replace("e = ", ""))
print(f"{n = }")
print(f"{e = }")

#get encrypted secret
s.sendlineafter(b"> " , b"1")
enc = int(s.recvline(0).decode())
newenc = (enc * pow(1234567890, e, n)) % n 

#s.interactive()
#get decrypted newenc 
s.sendlineafter(b"> " , b"3")
s.sendlineafter(b"10): ", str(newenc).encode())
newdec = int(s.recvline(0).decode().replace("Result : ", ""))
dec = (newdec * pow(1234567890, -1, n)%n)

print(f"Secret found : {ltb(dec)}")
