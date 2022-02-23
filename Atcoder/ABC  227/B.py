N = int(input())
S = [int(i) for i in input().split()]
pos = set()
for a in range(1, 1000 // 3 + 1):
    for b in range(1, 1000 // 3 + 1):
        area = 4*a*b + 3*a + 3*b
        if area > 1000:
            continue
        pos.add(area)
wrong = 0
for i in S:
    if i not in pos:
        wrong += 1
print(wrong)