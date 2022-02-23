s = input()
ans = ""
for a in s:
    if a == "B":
        if len(ans) != 0:
            ans = ans[:-1]
    else:
        ans += a
print(ans)