S = input()[::-1]
ans = ""
for s in S:
    if s == ">":
        ans += "<"
    else:
        ans += ">"
print(ans)