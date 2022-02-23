N = int(input())
C = [int(i) for i in input().split()]
me = float("inf")
ma = float("inf")
for i in range(N):
    ma = min(ma, C[i])
    if (i+1)&1:
        me = min(me, C[i])

subodd = 0
suball = 0
Q = int(input())
ts = 0
for _ in range(Q):
    S = input()
    if S[0] == "1":
        x,a = [int(i) for i in S[2:].split()]
        if x&1:
            if C[x-1] - subodd - suball >= a:
                C[x-1] -= a
                ts += a
                me = min(me, C[x-1])
                ma = min(ma, me)
        else:
            if C[x-1] - suball >= a:
                C[x-1] -= a
                ts += a
                ma = min(ma, C[x-1])
    elif S[0] == "2":
        a = int(S[2:])
        if me >= a:
            me -= a
            ma = min(ma, me)
            subodd += a
            ts += a*((N+1)//2)
    else:
        a = int(S[2:])
        if ma >= a:
            ma -= a
            me -= a
            suball += a
            ts += a*N
print(ts)