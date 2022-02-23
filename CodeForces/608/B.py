n = int(input())
b = [1 if i == "B" else 0 for i in input()]
sb = sum(b)
if sb % 2 == 1 and n % 2 == 0:
    print(-1)
elif sb == 0 or sb == n:
    print(0)
else:
    if sb > n//2:
        flip = 1
    else:
        flip = 0
    ans = []
    for a in range(len(b)-1):
        if b[a] == flip:
            # print(b)
            ans.append(a+1)
            b[a] = 1 - b[a]
            b[a+1] = 1 - b[a+1]
    print(len(ans))
    print(" ".join(map(str, ans)))