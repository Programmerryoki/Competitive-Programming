MOD = 10**9 + 7
n = int(input())
b = [int(i) for i in input().split()]
bac = 1
for a in b:
    bac *= 2
    bac -= a
    if bac < 0:
        print("error")
        break
else:
    print(bac%MOD)