T = int(input())

for case in range(T):
    N = int(input())
    matrix = [[int(i) for i in input().split()] for j in range(N)]
    trace = sum([matrix[i][i] for i in range(N)])
    repeatedRow = 0
    for i in range(N):
        if len(set(matrix[i])) != N:
            repeatedRow += 1

    repeatedCol = 0
    for i in range(N):
        if len(set([matrix[j][i] for j in range(N)])) != N:
            repeatedCol += 1
    print("Case #"+str(case+1)+":",trace, repeatedRow, repeatedCol)