n,a = map(int, input().split())
e = [int(i) for i in input().split()]
e.sort()
s = 0
n = 0
for i in e:
    if s + i < a:
        s += i + 1
        n += 1
    else:
        break
print(n)