n,m = [int(i) for i in input().split()]
s = [input() for i in range(n)]
ans = ""
i = 0
mid = ""
while i < len(s):
    l = s.pop()
    if l[::-1] == l:
        if len(mid) < len(l):
            mid = l
    elif l[::-1] in s:
        s.remove(l[::-1])
        ans += l

print(len(ans)*2+len(mid))
print(ans+mid+ans[::-1])