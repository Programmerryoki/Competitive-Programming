ans = "a"
print(ans, flush=True)
res = prev = int(input())
while res != -1 and res != 0:
    ans += "a"
    print(ans, flush=True)
    res = int(input())
    if res == prev:
        ans = ans[:-1] + "b"
    if res == prev == 1:
        ans = "b" + ans[1:]
