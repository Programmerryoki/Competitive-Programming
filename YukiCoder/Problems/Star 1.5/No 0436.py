S = input()
i = -1
while i < len(S) - 1 and S[i+1] == "c":
    i += 1
print(min(i, len(S) - i - 1))