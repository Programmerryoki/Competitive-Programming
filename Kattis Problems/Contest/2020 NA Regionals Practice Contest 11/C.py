N = int(input())
days = set()
for _ in range(N):
    s,t = map(int, input().split())
    for i in range(s,t+1):
        days.add(i)
print(len(days))