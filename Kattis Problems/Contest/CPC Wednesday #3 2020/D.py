from sys import stdin

vowel = "aeiouy"
for s in stdin.readlines():
    s = s.split()
    ans = []
    for a in s:
        if a[0] in vowel:
            ans.append(a+"yay")
        else:
            i = 0
            while a[i] not in vowel:
                i += 1
            ans.append(a[i:]+a[:i]+"ay")
    print(" ".join(ans))