f = open("output.txt", "r")
n = int(f.readline().strip().replace("n = ", ""))
e = int(f.readline().strip().replace("e = ", ""))
c = int(f.readline().strip().replace("c = ", ""))
truncate_p = int(f.readline().strip().replace("Truncated p = ", ""))

from Crypto.Util.number import long_to_bytes as ltb 
P.<x> = PolynomialRing(Zmod(n))
f = Integer(truncate_p) + x * 2 ^ (512 + 256)
f = f.monic()
ans = f.small_roots(beta = 0.4, X = 2^256, epsilon = 1/40)
print(ans)
if len(ans) == 0:
    print("No solution found!!!")
else:
    print(int(ans[0]).bit_length())
    p = truncate_p + ans[0] * 2 ^ (512 + 256)
    print(f"Found possible p : {p}")
    assert(gcd(p, n) != 1), "Not the right p!!!"
    q = n // int(p)
    d = pow(e, -1, (p-1)*(q-1))
    print("Message found : ")
    print(ltb(int(pow(int(c), int(d), n))))