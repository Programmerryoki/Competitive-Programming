n, l, k = [int(i) for i in input().split()]
word = input()
words = sorted(list(word))
ans = ["" for i in range(n)]
i = 0
for a in range(k):
    ans[a] += words[i]
    i += 1

if k-1 == 0 or (k-2 >= 0 and ans[k-1] != ans[k-2]):
    while len(ans[k-1]) < l:
        ans[k-1] += words[i]
        i += 1
else:
    while len(ans[k-1]) < l:
        for a in range(k):
            ans[a] += words[i]
            i += 1

for a in range(n):
    if a != k-1:
        length = l - len(ans[a])
        ans[a] += "".join(words[i:i+length])
        i += length

for a in ans:
    print(a)