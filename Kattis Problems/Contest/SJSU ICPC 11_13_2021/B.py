n,c,b = map(int, input().split())
z = [int(i) for i in input().split()]
ans = ["1" if c&1 else "0"] + ["0"] * b
ins = [""] * b
pv = 1
for i in range(b):
    d = z[i] - pv - 1
    pv = z[i]
    if d <= 0:
        continue
    if c == 0:
        break
    if d == 1:
        ins[i] = "1"
        c -= 2
    else:
        mincd = min(c // 2, d // 2)
        ins[i] = "10"*(mincd)
        c -= c//2
        if c == 0:
            break
        if d&1:
            ins[i] += "1"
            c -= 1
answer = ""
for i in range(len(ins)):
    if ins:
        answer += ans[i] + ins[i]
    else:
        break
print(answer + "0" * (n - len(answer)))