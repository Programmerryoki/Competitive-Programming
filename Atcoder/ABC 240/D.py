N = int(input())
a = [int(i) for i in input().split()]
c = 0
vals = []
ans = [0] * N
for i,v in enumerate(a):
    if vals and vals[-1][0] == v and vals[-1][1] == v-1:
        c -= v-1
        vals.pop()
    elif vals and vals[-1][0] == v:
        c += 1
        vals[-1][1] += 1
    elif (vals and vals[-1][0] != v) or not vals:
        c += 1
        vals.append([v, 1])
    ans[i] = c
print("\n".join(str(i) for i in ans))