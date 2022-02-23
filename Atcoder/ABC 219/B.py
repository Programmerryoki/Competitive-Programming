S = [input() for i in range(3)]
T = input()
ans = ""
for i in range(len(T)):
    if T[i] == "1":
        ans += S[0]
    elif T[i] == "2":
        ans += S[1]
    else:
        ans += S[2]
print(ans)