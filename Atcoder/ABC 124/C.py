S = input()
c = 0
for i in range(len(S)):
    if i&1:
        c += S[i] == "0"
    else:
        c += S[i] == "1"
print(min(c, len(S) - c))