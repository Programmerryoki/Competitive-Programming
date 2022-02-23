N = int(input())
ppl = []
lie = [0 for i in range(N)]
for a in range(N):
    A = int(input())
    temp = []
    for b in range(A):
        s = [int(i) for i in input().split()]
        temp.append(s)
