S = input()
i = len(S)-1
while i >= 0 and S[i] == "a":
    i -= 1
j = 0
while j < len(S) and S[j] == "a":
    j += 1
ls = len(S)
# print(S, ls-i-1, j)
S = S[j:i+1]
print("Yes" if S == S[::-1] and (ls-i-1) >= j else "No")