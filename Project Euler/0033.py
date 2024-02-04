from math import gcd
from functools import reduce
def div(a,b):
    ans = str(a // b) + '.'
    a %= b
    while a and len(ans) < 100:
        a *= 10
        ans += str(a // b)
        a %= b
    return ans

va, vb = 1, 1
for a in range(10,100):
    for b in range(a+1,100):
        sa = set(str(a))
        sb = set(str(b))
        if not (sa-sb and sb-sa) or len(sa | sb) != 3 or '0' in sa or '0' in sb:
            continue
        na = int((sa-sb).pop())
        nb = int((sb-sa).pop())
        if div(a,b) == div(na, nb):
            print(f"{a}/{b}, {na}/{nb} = {div(a,b)}")
            va *= a
            vb *= b
lcd = lambda x,y: x*y // gcd(x,y)
print(f"{va}/{vb}")