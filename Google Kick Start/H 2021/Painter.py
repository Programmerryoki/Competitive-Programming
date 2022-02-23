colorint = {"U":0,"R":1,"Y":2,"B":4,"O":3,"P":5,"G":6,"A":7}

T = int(input())
for case in range(T):
    N = int(input())
    P = input()
    colors = [colorint[p] for p in P]
    cont = [0] * 3
    stroke = 0
    for i in range(N):
        color = colors[i]
        for j in range(3):
            check = 1 << j
            if color & check:
                if cont[j] == 0:
                    stroke += 1
                    cont[j] = 1
            else:
                cont[j] = 0
    print(f"Case #{case+1}: {stroke}")