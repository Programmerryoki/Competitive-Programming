t = int(input())
for _ in range(t):
    S = input()
    p = 0
    res = len(S)
    for i,s in enumerate(S,1):
        if s == "+":
            p += 1
        else:
            p -= 1
        if p < 0:
            res += i
            p += 1
    print(res)