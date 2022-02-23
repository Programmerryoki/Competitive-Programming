N,M,K = [int(i) for i in input().split()]
P = [(int(i)*2)**2 for i in input().split()]
H = [(int(i)*2)**2 for i in input().split()]
S = [int(i)**2*2 for i in input().split()]
all = H + S
all.sort()
P.sort()
count = 0
j = 0
for i in P:
    if j < len(all) and i > all[j]:
        count += 1
        j += 1
print(count)