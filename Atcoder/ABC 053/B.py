s = input()
A = float("inf")
Z = -1
for i in range(len(s)):
    if s[i] == "A":
        A = min(A, i)
    elif s[i] == "Z":
        Z = max(Z, i)
print(Z - A + 1)