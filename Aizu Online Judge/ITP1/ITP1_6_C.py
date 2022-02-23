houses = [
    [[0]*10,[0]*10,[0]*10],
    [[0]*10,[0]*10,[0]*10],
    [[0]*10,[0]*10,[0]*10],
    [[0]*10,[0]*10,[0]*10]
]
n = int(input())
for a in range(n):
    b,f,r,v = [int(i) for i in input().split()]
    houses[b-1][f-1][r-1] += v

for i,house in enumerate(houses):
    for floor in house:
        print(" "+ " ".join(map(str, floor)))
    if i != len(houses)-1:
        print("#"*20)