word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rotate(s,r):
    ans = ""
    for a in s:
        ans += word[(word.index(a) + r)%26]
    return ans


msg = input()
s1 = msg[:len(msg)//2]
r1 = sum([word.index(i) for i in s1])%26
s2 = msg[len(msg)//2:]
r2 = sum([word.index(i) for i in s2])%26
s1 = rotate(s1, r1)
s2 = rotate(s2, r2)
ans = ""
for a in range(len(s1)):
    ans += word[(word.index(s1[a]) + word.index(s2[a]))%26]
print(ans)