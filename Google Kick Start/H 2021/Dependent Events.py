from collections import deque
from fractions import Fraction
den = 10**6
inf = Fraction(10**10, 1)
MOD = 10**9 + 7

print(Fraction(10352,100000))

T = int(input())
for case in range(T):
    N,Q = [int(i) for i in input().split()]
    p1 = int(input())
    graph = {i+1:set() for i in range(N)}
    condprob = []
    for cur in range(N-1):
        P,A,B = [int(i) for i in input().split()]
        condprob.append((Fraction(A,den),Fraction(B,den)))
        graph[P].add(cur+2)
    print(graph)
    prob = [[Fraction(0,1), Fraction(0,1)] for _ in range(N)]
    prob[0] = [Fraction(p1,den), Fraction(10**6 - p1,den)]
    que = deque([1])
    while que:
        cur = que.popleft()
        pc = prob[cur-1]
        for nxt in graph[cur]:
            tmp = prob[nxt-1]
            pos, neg = condprob[nxt-2]
            tmp[0] = pos * pc[0] + neg * pc[1]
            tmp[1] = Fraction(1,1) - tmp[0]
            que.append(nxt)
    print(prob)
    ans = []
    for _ in range(Q):
        u,v = [int(i) for i in input().split()]
        tmp = prob[u-1][0] * prob[v-1][0]
        print(tmp, float(tmp))
        ans.append(pow(tmp.denominator, -1, MOD) * tmp.numerator)
    print(f"Case #{case+1}: {' '.join(map(lambda x: str(x % MOD), ans))}")