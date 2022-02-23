n,m = [int(i) for i in input().split()]
for _ in range(n):
    if "LOVE" in input():
        print("YES")
        break
else:
    print("NO")