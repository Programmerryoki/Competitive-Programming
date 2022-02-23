from itertools import permutations

steps = [int(i) for i in input().split()]
pos = list(permutations(steps, 4))
ma = 0
area = 0
for step in pos:
    if step[0] >= step[2] and step[1] <= step[3]:
        area = min(step[0], step[2]) * min(step[1], step[3])
        if area > ma:
            ma = area
print(ma)