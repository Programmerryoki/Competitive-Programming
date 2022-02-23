h, w = [int(i) for i in input().split()]
s = [input() for i in range(h)]
seen = []

def around(a,b):
    c = 0
    if a+1 < h and s[a+1][b] == "." and [a+1, b] not in seen:
        c += 1
    if b+1 < h and s[a][b+1] == "." and [a, b+1] not in seen:
        c += 1
    if a-1 >= 0 and s[a-1][b] == "." and [a-1, b] not in seen:
        c += 1
    if b-1 >= 0 and s[a][b-1] == "." and [a, b-1] not in seen:
        c += 1
    return c

for a in range(h):
    for b in range(w):
        c = around(a,b)
        if c <= 2:
            seen.append([a,b])
print(seen)