dic = {}
N = int(input())
for _ in range(N):
    s = input()
    dic.setdefault(s, 0)
    dic[s] += 1
M = int(input())
for _ in range(M):
    s = input()
    try:
        dic[s] -= 1
    except:
        continue
m = 0
for k in dic:
    m = max(m, dic[k])
print(m)