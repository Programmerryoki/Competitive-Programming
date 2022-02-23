N = int(input())
A = [int(i) for i in input().split()]
count = {i:0 for i in range(8)}
over = 0
for a in A:
    if a < 3200:
        count[a//400] = 1
    else:
        over += 1
hp = sum(count.values())
print(hp + int(hp == 0), hp + over)