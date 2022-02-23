S = list(input())
for i in range(len(S)):
    if S[i] in {"I","l"}:
        S[i] = 1
    elif S[i] in {"O", "o"}:
        S[i] = 0
print("".join(map(str, S)))