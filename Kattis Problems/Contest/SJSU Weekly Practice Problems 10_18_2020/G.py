from math import ceil
anss = []
while True:
    t = []
    n = int(input())
    if n == 0:
        break

    ans = [eval(input()) for i in range(n)]
    ml = len(str(max(ans, key=lambda x: len(str(x)))))
    opl = 50 // (ml + 1)
    for i in range(ceil(n / opl)):
        t.append(" ".join(map(lambda x: " "*(ml - len(str(x))) + str(x), ans[opl*i:opl*i+opl])))
    anss.append(t)
print("\n\n".join("\n".join(i) for i in anss))