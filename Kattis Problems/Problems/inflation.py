n = int(input())
gas = list(sorted([int(i) for i in input().split()]))
mi = 1
c = 0
for a in range(1,len(gas)+1):
    if gas[a-1] > a:
        c = 1
        break
    else:
        mi = min(mi, gas[a-1]/a)
if c == 0:
    print(mi)
else:
    print("impossible")