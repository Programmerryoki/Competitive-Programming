conv = " abcdefghijklmnopqrstuvwxyz"

def encryption(s):
    u = conv.index(s[0])
    ans = s[0]
    for a in s[1:]:
        u = u + conv.index(a)
        ans += conv[u%27]
    return ans

def decryption(s):
    sn = list(reversed([conv.index(i) for i in s]))
    ans = ""
    for a in range(len(sn)-1):
        n = sn[a]-sn[a+1]
        if n < 0:
            n += 27
        ans = conv[n] + ans
    ans = s[0] + ans
    return ans

n = int(input())
for a in range(n):
    s = input()
    t = s[0]
    s = s[s.index(" ")+1:]
    ans = ""
    if t == "e":
        ans = encryption(s)
    elif t == "d":
        ans = decryption(s)
    print(ans)