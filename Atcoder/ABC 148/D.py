N = int(input())
a = [int(i) for i in input().split()]
c = 1
i = 0
while i < len(a):
    try:
        i = a.index(c,i)
        c += 1
    except:
        break
if c == 1:
    print(-1)
else:
    print(len(a)-c+1)