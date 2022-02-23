from collections import Counter
import math
from math import factorial

t = int(input())
for _ in range(t):
    #######################
    # finding fingerprint #
    #######################
    k = int(input())
    ori = []
    n = k
    div = 2
    while n != 0:
        # print(n)
        ori.append(n%div)
        n //= div
        div += 1
    print("finger",ori)
    count = list(Counter(ori).values())
    # print(count)

    ##################################
    # creating grid for rooks number #
    ##################################

    # change to set or not set
    # ori = list(set(ori))

    ori.sort()
    oriG = [i for i in ori if i > 0]
    ma = max(ori)
    n = len(ori)
    matrix = [[1 if ori[i] > a+1 else 0 for a in range(n)] for i in range(n)]
    # for a in matrix:
    #     print(a)

    ###################################
    # reducing board to smaller parts #
    ###################################
    i = 0
    while i < len(matrix[0]):
        if sum([a[i] for a in matrix]) == 0:
            for a in range(n):
                matrix[a].pop(i)
        else:
            i += 1
    i = 0
    while i < len(matrix):
        if sum(matrix[i]) == 0:
            matrix.pop(i)
        else:
            i += 1
    print("Printing Matrix....")
    for a in matrix:
        print(a)

    if len(matrix) == 0:
        print(0)
    else:
        #####################################
        # actually finding rooks polynomial #
        #####################################
        n = len(matrix)
        m = len(matrix[0])
        mi = min(n,m)
        rook = [0 for i in range(mi)]
        answers = [[] for i in range(mi)]

        def rooks(M,r):
            # print("r",r)
            # for a in M:
            #     print(a)

            if r == mi:
                if M not in answers[r-1]:
                    answers[r-1].append(M)
                    # print("###############")
                    return 1
                else:
                    return 0
            elif r > 0:
                if M not in answers[r-1]:
                    answers[r-1].append(M)
                else:
                    return 0

            t = 0
            pos = []
            for a in range(n):
                for b in range(m):
                    if M[a][b] != 1 and sum(M[a]) == 0 and sum([i[b] for i in M]) == 0 and matrix[a][b] == 1:
                        MA = [[M[ja][ia] for ia in range(m)] for ja in range(n)]
                        MA[a][b] = 1
                        # t += rooks(MA, r+1)
                        # for hhhh in MA:
                        #     print("\t",hhhh)
                        # print()
                        pos.append(MA)
            # print(pos)
            for a in pos:
                t += rooks(a,r+1)
            rook[r] += t
            return 0

        rooks([[0 for i in range(m)] for j in range(n)],0)
        print("oriG",oriG)

        # print("mi",mi)
        for a in range(len(answers)):
            for b in range(len(answers[a])):
                # print(answers[a][b])
                answers[a][b] = [oriG[i] for i in range(len(answers[a][b])) if sum(answers[a][b][i]) > 0]
                # print(answers[a][b])


        for a in range(len(rook)):
            # print(answers[a])
            answers[a] = set(",".join(map(str, i)) for i in answers[a])
            print(answers[a])
            rook[a] = len(answers[a])


            num = []
            for b in answers[a]:
                f = [i for i in ori]
                b = [int(i) for i in b.split(",")]
                for i in b:
                    f.remove(i)
                cb = list(Counter(f).values())
                number = factorial(len(f))
                for nn in cb:
                    number /= factorial(nn)
                num.append(number)
                print(f,b)
            answers[a] = num


        print("Rooks Poly:",rook)

        ans = factorial(len(ori))
        ans1 = factorial(len(ori))
        for a in range(len(rook)):
            if a%2==0:
                ans -= rook[a] * factorial(len(ori) - a - 1)
                ans1 -= sum(answers[a])
            else:
                ans += rook[a] * factorial(len(ori) - a - 1)
                ans1 += sum(answers[a])
        print(ans, ans1)
        for a in count:
            ans /= factorial(a)
            ans1 /= factorial(a)
        print(ans, ans1)

        # for a in range(len(answers)):
        #     for b in answers[a]:
        #         print()
        #         for c in b:
        #             print("\t"*a,c)
        print(answers)