words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
s = input()
ans = ""
for w in s:
    ans += words[(n+words.index(w))%26]
print(ans)