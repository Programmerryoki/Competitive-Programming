n = int(input())
p = [int(i) for i in input().split()]
m = max(p)+1
c = 0
for num in p:
    if num < m:
        c += 1
        m = num
print(c)