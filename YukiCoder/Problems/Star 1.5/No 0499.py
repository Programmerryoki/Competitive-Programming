N = int(input())
ans = ""
while N != 0:
    ans = str(N%7) + ans
    N //= 7
if ans != "":
    print(ans)
else:
    print(0)