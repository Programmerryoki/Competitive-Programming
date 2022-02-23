# L,R = [int(i) for i in input().split()]
n = []
cum = [0]
for i in range(1, 20):
    n.append(len(str(i)) * i)
    cum.append(cum[-1] + n[-1])
print(n)
print(cum)