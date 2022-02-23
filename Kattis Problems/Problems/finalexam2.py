n = int(input())
ans = [input() for i in range(n)]
count = 0
for i in range(n-1):
    count += (ans[i] == ans[i+1])
print(count)