h,w,n = map(int, input().split())
x = [int(i) for i in input().split()]
l = 0
H = 0
for i in x:
    l += i
    if l > w:
        print("NO")
        exit()
    elif l == w:
        l = 0
        H += 1
        if H == h:
            print("YES")
            exit()
print("YES" if H == h else "NO")