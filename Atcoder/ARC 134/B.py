N = int(input())
s = input()
words = [[] for _ in range(26)]
for i in range(len(s)):
    words[ord(s[i])-ord("a")].append(i)
last = N
s = list(s)
used = set()
for i in range(N):
    if i in used:
        continue
    for ind in range(ord(s[i])-ord("a")):
        if not words[ind]:
            continue
        elif words[ind][0] > last:
            words[ind] = []
            continue
        for j in range(len(words[ind])-1, -1, -1):
            if words[ind][j] > last:
                continue
            break
        swap = words[ind][j]
        words[ind] = words[ind][:j]
        if swap not in used:
            last = swap
            s[i], s[swap] = s[swap], s[i]
            used.add(i)
            used.add(swap)
            break
    used.add(i)
print("".join(s))