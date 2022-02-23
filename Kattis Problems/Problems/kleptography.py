word = "abcdefghijklmnopqrstuvwxyz"

n, m = [int(i) for i in input().split()]
key = input()
text = input()
key = text[:len(text) - len(key)] + key
print(key)
print(text)
ans = ""
for a in range(len(text)):
    ans += word[(word.index(text[a]) + word.index(key[a]))%26]
print(ans)