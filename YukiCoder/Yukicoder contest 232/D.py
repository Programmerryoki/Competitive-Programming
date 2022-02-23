N = int(input())
S = input()
A = [int(i) for i in input().split()]
Q = int(input())
K = [int(i) for i in input().split()]

ans = []
E = sum([1 for i in range(len(S)) if S[i] == "E"])
SA = sum(A)

ansl = [[i] for i in set(K)]
for i, a in enumerate(ansl):
    pos = 