from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl 
from gmpy2 import iroot 

def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return x
def fermat(n):
	t0=isqrt(n)+1
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)
	while((temp*temp)!=((t*t)-n)):
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	return p,q

f = open("output.txt", "r")
n = int(f.readline().replace("n = ", "").strip())
e = int(f.readline().replace("e = ", "").strip())
c = int(f.readline().replace("c = ", "").strip())

p, q = fermat(n)
print(f"Found p = {p}")
print(f"Found q = {q}")
d= pow(e, -1, (p-1)*(q-1))
print("Message found : ")
print(ltb(pow(c,d,n)))