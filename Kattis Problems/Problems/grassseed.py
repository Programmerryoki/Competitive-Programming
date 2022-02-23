cost = float(input())
n = int(input())
lawn = 0
for a in range(n):
    length = list(map(float, input().split()))
    lawn += length[0] * length[1]
print(lawn * cost)