N = int(input())
E = int(input())

villager = [0] * N

for a in range(E):
    event = list(map(int, input().split()))[1:]
    if 1 in event:
        for b in event:
            villager[b-1] += 1
    else:
        ma = max([villager[i - 1] for i in event])
        for b in event:
            villager[b-1] = ma
    #print(villager)

ma = villager[0]
for i, a in enumerate(villager):
    if a == ma:
        print(i+1)
#print(villager)