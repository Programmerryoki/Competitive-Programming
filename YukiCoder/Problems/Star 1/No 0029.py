N = int(input())
item = {}
for _ in range(N):
    drop = [int(i) for i in input().split()]
    for i in drop:
        try:
            item[i] += 1
        except:
            item[i] = 1
pu = 0
ex = 0
for k in item.keys():
    pu += item[k]//2
    ex += item[k]%2
pu += ex//4
print(pu)