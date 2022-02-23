S = input()
T = input()
sa = [ord(i)-ord("a") for i in S]
c = False
d = 0
for i,w in enumerate(T):
    n = ord(w) - ord("a")
    if not c and n == sa[i]:
        continue
    if not c:
        d = n - sa[i]
        c = True
    if n != (sa[i] + d)%26:
        print("No")
        break
else:
    print("Yes")