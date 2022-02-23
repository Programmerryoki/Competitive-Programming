S = int(input())
s = S%60
S //= 60
m = S%60
S //= 60
print(str(S) + ":" + str(m) + ":" + str(s))