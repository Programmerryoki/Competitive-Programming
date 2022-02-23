T = int(input())
for _ in range(T):
    N = [int(i) for i in input().split()]
    N[1] //= 2
    mv = 0
    def dfs(n2,n6,n4,total):
        global mv
        mv = max(mv, total)
        if n2 >= 5:
            dfs(n2%5, n6, n4, total + n2//5)
        if n2 >= 3 and n4:
            m = min(n2//3, n4)
            dfs(n2-(3*m), n6, n4-m, total + m)
        if n2 >= 2 and n6:
            m = min(n2//2, n6)
            dfs(n2-(2*m), n6-m, n4, total + m)
        if n2 and n4 >= 2:
            m = min(n2, n4//2)
            dfs(n2-m, n6, n4-(2*m), total + m)
        if n6 and n4:
            m = min(n4, n6)
            dfs(n2, n6-m, n4-m, total + m)

    dfs(N[0], N[1], N[2], 0)
    print(mv)