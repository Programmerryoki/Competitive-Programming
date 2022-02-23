t = int(input())
for _ in range(t):
    key = input()
    s = input()
    k = s[0]
    tt = 0
    for i in s:
        tt += abs(key.index(k) - key.index(i))
        k = i
    print(tt)