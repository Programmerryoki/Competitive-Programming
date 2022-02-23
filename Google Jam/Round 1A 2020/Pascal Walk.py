from math import factorial
from functools import reduce
import sys
sys.setrecursionlimit(100000)

def comb(r, k):
    r -= 1
    k -= 1
    return reduce(lambda x,y: x*y, [1]+[i for i in range(r, k, -1)]) // factorial(r-k)

T = int(input())
for case in range(T):
    N = int(input())
    print("Case #"+str(case+1)+":")
    path = []
    def recur(vi, r, k, s):
        global path
        if path != []:
            return
        if len(path) > 500:
            return
        if s == N:
            path = vi
            return
        elif s > N:
            return

        pos = [(r, k+1),(r+1, k),(r+1, k+1),(r-1, k-1),(r-1, k),(r, k-1)]
        for ri, ki in pos:
            if (ri,ki) not in vi:
                if 1 <= ri and 1 <= ki <= ri:
                    # print(ri,ki)
                    recur(vi+[(ri,ki)], ri, ki, s+comb(ri,ki))
    recur([(1,1)], 1, 1, 1)
    print("\n".join(str(i)+" "+str(j) for i,j in path))
    # t = 0
    # for i,j in path:
    #     n = comb(i,j)
    #     t += n
    #     print(n, (i,j))
    # print(t)