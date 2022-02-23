N = int(input())
names = set()
for _ in range(N):
    S,T = input().split()
    if (S,T) in names:
        print("Yes")
        exit()
    names.add((S,T))
print("No")