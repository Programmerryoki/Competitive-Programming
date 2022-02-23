from heapq import heappush, heappop, heapify

N = int(input())
players = [tuple(int(i) for i in input().split()) for _ in range(N)]
adding = [i[0] for i in players]
heapify(adding)
sub = [i[0]+i[1]-1 for i in players]
heapify(sub)
count = [0]*N
s = 0
i = 0; j = 0
pd = adding[0]
while adding and sub:
    cd = min(adding[0], sub[0])
    while adding and adding[0] == cd:
        s += 1
        heappop(adding)
    print(s, cd,pd, cd-pd,adding,sub)
    if s:
        count[s-1] += cd - pd
        pd = cd
    while sub and sub[0] == cd:
        s -= 1
        heappop(sub)
print(" ".join(map(str, count)))