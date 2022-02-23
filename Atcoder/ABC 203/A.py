a,b,c = map(int, input().split())
if a == b:
    print(c)
elif a == c:
    print(b)
elif c == b:
    print(a)
else:
    print(0)