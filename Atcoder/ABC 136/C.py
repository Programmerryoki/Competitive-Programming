N = int(input())
H = [int(i) for i in input().split()]
m = H[0]
for h in H:
    if m - h > 1:
        print("No")
        break
    m = max(m, h)
else:
    print("Yes")