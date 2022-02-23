while True:
    n = int(input())
    if n == -1:
        break
    matrix = [[int(i) for i in input().split()] for j in range(n)]
    ans = []
    for i in range(n):
        has_nei = False
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[k][i] == 1:
                        has_nei = True
                        break
                if has_nei:
                    break
        if not has_nei:
            ans.append(i)
    print(" ".join(map(str, ans)))