N = int(input())
dic = {}
for _ in range(N):
    s = input()
    dic.setdefault(s, 0)
    dic[s] += 1
ans = list(dic.items())
ans.sort(key=lambda x: (-x[1], x[0]))
m = ans[0][1]
print("\n".join(i[0] for i in ans if i[1] == m))