from collections import Counter

M = int(input())
users = {}
for _ in range(M):
    name, *keys = input().split()
    ws = Counter(keys)
    if name in users:
        users[name].update(ws)
    else:
        users[name] = ws
# print(users)
ans = Counter({i:0 for i in users[list(users.keys())[0]]})
# print(ans)
for key in users:
    same = ans.keys() & users[key].keys()
    ans = Counter({k: ans[k] + users[key][k] for k in same})
if not ans:
    print("ALL CLEAR")
    exit()
ans = list(ans.most_common())
ans.sort(key=lambda x: (-x[1], x[0]))
# print(ans)
print("\n".join(i[0] for i in ans))