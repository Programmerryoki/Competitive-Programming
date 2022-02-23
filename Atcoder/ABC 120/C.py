S = input()
n = 0
i = 0
while i < len(S):
    # print(S)
    if len(set(S[i:i+2])) == 2:
        S = S[:i]+S[i+2:]
        n += 2
        if i != 0:
            i -= 1
    else:
        i += 1
print(n)