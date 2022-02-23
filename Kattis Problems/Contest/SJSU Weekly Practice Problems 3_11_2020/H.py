from collections import defaultdict

ani = input()
n = int(input())
order = []
pos = defaultdict(int)
np = []
for a in range(n):
    name = input()
    order.append(name)
    if name[0] == ani[-1]:
        pos[name] = 0
    else:
        np.append(name)
for name in np:
    for b in pos.keys():
        if name[0] == b[-1]:
            pos[b] += 1

if len(pos) == 0:
    print("?")
else:
    p = [[pos[i], i] for i in pos.keys()]
    p.sort(key = lambda x: (x[0], order.index(x[1])))
    ans = p[0]
    if ans[0] == 0:
        print(ans[1] + "!")
    else:
        print(ans[1])