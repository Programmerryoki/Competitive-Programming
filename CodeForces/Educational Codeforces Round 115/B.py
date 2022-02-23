t = int(input())
for _ in range(t):
    n = int(input())
    stu = [[int(i) for i in input().split()] for j in range(n)]
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            stu.sort(key=lambda x: (x[i], -x[j]), reverse=True)
            if stu[(n-1)//2][i] == 0:
                continue
            if sum([1 if stu[k][j] == 1 else 0 for k in range(n//2, n)]) == n//2:
                break
        else:
            continue
        print("YES")
        break
    else:
        print("NO")