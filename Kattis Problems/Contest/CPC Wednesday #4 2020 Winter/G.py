from math import ceil

ans = 500
s = 250
print(ans)
res = input()
while res != "correct":
    if res == "lower":
        ans -= s
    elif res == "higher":
        ans += s
    if ans <= 0:
        ans = 1
    elif ans > 1000:
        ans = 1000
    s = ceil(s/2)
    print(ans, flush=True)
    res = input()