t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    if abs(a-b) <= 1:
        ans = [i for i in range(0,a+b+1,2)]
    else:
        ans = [i for i in range(1,a+b+1,2)]
    print(" ".join(str(i) for i in ans))