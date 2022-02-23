N = int(input())
t = [int(i) for i in input().split()]
t.sort(reverse=True)
d = 1
for i in range(N):
    d = max(d, t[i]+i+1)
print(d+1)