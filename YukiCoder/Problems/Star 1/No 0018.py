w = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = list(input())
for i in range(len(s)):
    s[i] = w[(w.index(s[i]) - i - 1 + 26*10000)%26]
print("".join(s))