c = 0
while True:
    try:
        matrix = [[int(i) for i in input().split()] for j in range(2)]
        c += 1
    except:
        break
    input()

    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    inv = int(1 / det)
    print("Case "+str(c)+":")
    for i,a in enumerate(matrix):
        for j,b in enumerate(a):
            matrix[i][j] = b * inv
    matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
    matrix[0][1], matrix[1][0] = -matrix[0][1], -matrix[1][0]
    print("\n".join(" ".join(map(str, i)) for i in matrix))