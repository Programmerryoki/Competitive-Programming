N = int(input())
names = {}
for _ in range(N):
    S = input()
    if S not in names:
        names[S] = 0
    names[S] += 1
print(max(names, key=lambda x: names[x]))