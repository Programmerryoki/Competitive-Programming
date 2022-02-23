N = int(input())
days = []
for a in range(N):
    event = [int(i) for i in input().split()]
    for b in range(event[0], event[1] + 1):
        if b not in days:
            days.append(b)
print(len(days))