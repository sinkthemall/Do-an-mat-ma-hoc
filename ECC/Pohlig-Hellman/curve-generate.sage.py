

# This file was *autogenerated* from the file curve-generate.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_128 = Integer(128); _sage_const_256 = Integer(256); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10)
from argparse import ArgumentParser
import sys
from sage.all import *


parser = ArgumentParser("Generate task on Pohlig-Hellman algo")
parser.add_argument("--p-start", type=int, default=_sage_const_2 **_sage_const_128 , help="min(p)")
parser.add_argument("--p-stop", type=int, default=_sage_const_2 **_sage_const_256 , help="max(p)")

if __name__ == "__main__":
    args = parser.parse_args()

    p = random_prime(args.p_stop, lbound=args.p_start)
    F = GF(p)
    E = None

    print(f"Finding curve with smooth order over field {F}", file=sys.stderr)
    while True:
        a, b = randint(_sage_const_1 , p), randint(_sage_const_1 , p)
        E_t = EllipticCurve(F, [a, b])
        print(E_t)
        order = E_t.order()
        print(f"Order = {order}")
        print(f"{order} = ", end="", file=sys.stderr)
        print(factor(order), file=sys.stderr)
        print("Countinue?[y]", file=sys.stderr)
        answer = input().lower()
        if "y" in answer:
            E = E_t
            E.set_order(order)
            break
    
    G = E.gens()[_sage_const_0 ]
    d = randint(E.order() // _sage_const_10 , E.order() - _sage_const_1 )
    P = d * G
    print(f"{P} = {d}*{G}", file=sys.stderr)
    print(f"{P} = d*{G}")
    print(f"d = ?")
    

